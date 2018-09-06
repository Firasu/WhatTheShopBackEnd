from rest_framework.permissions import BasePermission

class IsExpertorStaff(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.user == object.expert or request.user_is_staff:
            return True
        return False
