from rest_framework import permissions

class CustomReadOnly(permission.BasePermission):
    def has_object_permission(self, request, view, obj):        # GET : 누구나, PUT/PATCH: 해당 유저 
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user