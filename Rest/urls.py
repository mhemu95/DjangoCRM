from django.urls import path
from . import views


app_name = 'rest'

urlpatterns = [
    path('new/', views.TestView.as_View(), name='new'),
]