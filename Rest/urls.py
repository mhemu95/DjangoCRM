from django.urls import path
from . import views


app_name = 'rest'

urlpatterns = [
    path('students/', views.studentView, name='students'),
    path('students/detail/<str:pk>/', views.studentDetail, name='student-detail'),

    path('students-create/', views.studentCreate, name='student-create'),
    path('students-update/<str:pk>/', views.studentUpdate, name='student-update'),
    path('students-delete/<str:pk>/', views.studentDelete, name='student-delete'),

]
