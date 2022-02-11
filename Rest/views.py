from urllib import response
from webbrowser import get
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer

# Create your views here.


@api_view(['GET'])
def studentView(request):
    students = Student.objects.all()
    serialize = StudentSerializer(students, many=True)

    return Response(serialize.data)


@api_view(['GET'])
def studentDetail(request, pk):
    students = Student.objects.get(id=pk)
    serialize = StudentSerializer(students, many=False)

    return Response(serialize.data)


@api_view(['POST'])
def studentCreate(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def studentUpdate(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def studentDelete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    return Response("Student information deleted successfully.")
