from rest_framework import permissions

class IsSuperuserPermission(permissions.BasePermission):
    
    # def has_permission(self, request, view):
    #     # import pdb;pdb.set_trace()
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
        
    #     elif request.method=='DELETE':
    #         return request.user.is_superuser
        
    #     return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # import pdb;pdb.set_trace()
        elif obj.owner==request.user or request.user.is_superuser:
            return True
        
        return False
    