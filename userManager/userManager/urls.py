from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('userProfile_app.api.urls')),
    path('', include('Bank_System.api.urls')),
]
