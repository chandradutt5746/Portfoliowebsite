from django.shortcuts import render
from .models import Project, ContactMessage
from .serializers import ProjectSerializer, ContactMessageSerializer, ContactMessage
from rest_framework.generics import RetrieveAPIView
from rest_framework import viewsets, status
from django.http import HttpResponse
from rest_framework.response import Response
# Create your views here.


def index(request):
    return HttpResponse("Welcome to Chandradutt Patel's Portfolio API")


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
