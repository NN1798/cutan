from rest_framework import permissions


METHOD_UPDATE = ('PATCH', 'PUT')

class PostAuthenticatedUpdateOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True
    

    def has_object_permission(self, request, view, obj):
        if request.method in METHOD_UPDATE:
            return request.user == obj.user
        return True