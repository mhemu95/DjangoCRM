from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path('', views.Lead_list, name="leadList"),
    path('detail/<int:pk>/', views.Lead_detail, name="leadDetail"),
    path('create/', views.Lead_create, name="leadCreate"),

]