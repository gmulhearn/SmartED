from django.http import HttpResponse
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer