from django.urls import path
from .views import StudentApiView


app_name = 'rest'

urlpatterns = [
    path('students/', StudentApiView.as_view(), name='students'),
    
]