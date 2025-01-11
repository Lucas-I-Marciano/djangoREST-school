from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # SAFE_METHODS:  ('GET', 'HEAD', 'OPTIONS')
            return True
        
        if request.user == obj.owner : # obj:  Snippet object (i) => i=instance
            return True