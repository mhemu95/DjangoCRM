from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path('', views.Lead_list, name="leadList"),
    path('detail/<pk>/', views.Lead_detail, name="leadDetail"),

]