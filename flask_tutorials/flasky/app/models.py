import os
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
# Flask-Login works closely with the application’s own User objects. To be able to work
# with the application’s User model, the Flask-Login extension requires it to implement
# a few common properties and methods.

from flask_login import UserMixin

class Permission:
    FOLLOW=1
    COMMENT=2
    WRITE=4
    MODERATE=8
    ADMIN=16

class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default=db.Column(db.Boolean, default=False, index=True)
    permission=db.Column(db.Integer)
    users=db.relationship('User', backref='role', lazy='dynamic')
    
    def __init__(self, *args, **kwargs):
        super(Role, self).__init__(*args, **kwargs)
        if self.permission is None:
            self.permission = 0
    
    def __repr__(self):
        return '<Role %r>' % self.name
    
    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permission+=perm
    
    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permission-=perm
    
    def reset_permission(self, perm):
        self.permission=0
    
    def has_permission(self, perm):
        return self.permission & perm==perm
    
    @staticmethod
    def insert_roles():
        roles = {
            'User':[Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
            'Moderator':[Permission.FOLLOW, Permission.COMMENT, Permission.WRITE,
                         Permission.MODERATE],
            'Administrator':[Permission.FOLLOW, Permission.COMMENT,
                            Permission.WRITE, Permission.MODERATE,
                            Permission.ADMIN],
        }
        
        default_role='User'
        for r in roles:
            role=Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permission()
            for perm in role[r]:
                role.add_permission(perm)
            role.default = (role.name==default_role)
            db.session.add(role)
            db.session.commit()
    
class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash=db.Column(db.String(128))
    email=db.Column(db.String(64), unique=True, index=True)
        
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    
    @password.setter
    def password(self, password):
        self.password_hash=generate_password_hash(password)
    
    def verify_password(self, passowrd):
        return check_password_hash(self.password_hash, passowrd)
    
    # The login_manager.user_loader decorator is used to register the function with
    # Flask-Login, which will call it when it needs to retrieve information about the logged-
    # in user.
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return '<User %r>' % self.username
    
    
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        if self.role is None:
            if self.email=='abc@def.com':
                self.role == Role.query.filter_by(name="Administrator")
            if self.role is None:
                self.role=Role.query.filter_by(default=True).first()
    
    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)
    

class AnonymousUser(AnonymousUserMixin):
    def can(self, Permission):
        return False
    
    def is_administrator(self):
        return False

login_manager.anonymous_user=AnonymousUser
                

