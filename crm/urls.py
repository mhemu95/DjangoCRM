from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework')),
    path('rest/', include('Rest.urls', namespace="rest")),
    path('leads/', include('main.urls', namespace="leads")),
]
