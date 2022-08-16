from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.template.loader import get_template
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import TaskSerializer, ListSerializer
from ..models import Task, List


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    template = get_template("list_li.html")

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return List.objects.filter(user=user)

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            result = ListViewSet.template.render(context=serializer.data)
            return HttpResponse(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, pk=None):
        try:
            list_obj = List.objects.get(id=pk)
            list_obj.delete()
            return HttpResponse(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    patch_template = get_template("task_completed_button.html")
    template = get_template("task_li.html")

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Task.objects.filter(parent_list=user)

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = TaskViewSet.template.render(context=serializer.data)
            return HttpResponse(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request: Request, pk=None) -> Response:
        try:
            task_obj: Task = Task.objects.get(id=pk)
            task_obj.completed = not task_obj.completed
            task_obj.save()
            context = {
                'id': pk, 'title': task_obj.title, 
                'completed': task_obj.completed,
                'parent_list': task_obj.parent_list}

            result = TaskViewSet.patch_template.render(context=context)
            return HttpResponse(result, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            pass

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, pk=None):
        try:
            task_obj = Task.objects.get(id=pk)
            task_obj.delete()
            return HttpResponse(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
