from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Hello World!!!!!!!!")

urlpatterns = [
    path('', home, name="name"),
]