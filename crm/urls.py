from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('leads/', include('main.urls', namespace="leads")),

    path('', include('Rest.urls', namespace="rest")),

]
