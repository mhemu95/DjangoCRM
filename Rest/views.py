from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentApiView(APIView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serialize = StudentSerializer(students)
        return Response(serialize.data)
