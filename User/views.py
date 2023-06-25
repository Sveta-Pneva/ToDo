from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from rest_framework.viewsets import GenericViewSet

from .models import CustomUser
from .serializers import CustomUserFullModelSerializer, CustomUserModelSerializer

class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class CustomUserPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = "page_size"

class CustomUserModelViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
    pagination_class = CustomUserPagination

    def get_serializer_class(self):
        if self.request.version == "2.0":
            return CustomUserFullModelSerializer
        return CustomUserModelSerializer