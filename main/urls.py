from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path('', views.Lead_list, name="leadList"),
    path('create/', views.Lead_create, name="leadCreate"),
    path('detail/<int:pk>/', views.Lead_detail, name="leadDetail"),
    path('<int:pk>/update/', views.Lead_update, name="leadUpdate"),
    path('<int:pk>/delete/', views.Lead_delete, name="leadDelete"),

]