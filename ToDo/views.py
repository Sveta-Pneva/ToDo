from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .filters import ProjectFilter, TodoFilter
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer

class PageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"

class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()
    filterset_class = ProjectFilter
    pagination_class = PageNumberPagination

class ToDoPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"

class ToDoModelViewSet(ModelViewSet):
    serializer_class = ToDoModelSerializer
    queryset = ToDo.objects.all()
    filterset_class = TodoFilter
    pagination_class = ToDoPagination

    def destroy(self, request, pk=None):
        instance = get_object_or_404(ToDo, pk=pk)
        instance.is_active = False
        instance.save()
        todoobj = ToDo.objects.all()
        serializer_class = ToDoModelSerializer(todoobj, many=True)
        return Response(serializer_class.data)