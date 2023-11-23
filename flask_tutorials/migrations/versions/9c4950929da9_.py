"""empty message

Revision ID: 9c4950929da9
Revises: 
Create Date: 2023-10-25 15:37:32.046434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c4950929da9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('users_role_id_fkey', type_='foreignkey')
        batch_op.drop_column('role_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('users_role_id_fkey', 'roles', ['role_id'], ['id'])

    # ### end Alembic commands ###
