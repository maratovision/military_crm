from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.groups.filter(name__in=['president']) or request.user.is_superuser:
            return True


class FilterObjectPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            user_group = request.user.groups.filter(name__in=['sergeant', 'general', 'president'])
            doc = obj.document_root in ['Public', 'Private', 'Secret', 'Top-Secret']
            if user_group and doc:
                return True
