from django.urls import path
from Bank_System.api.views import UserListAV, UserDetailAV, BankListAV, BankDetailAV, TakaListAV, TakaDetailAV


urlpatterns = [
    path('userlist/',UserListAV.as_view(), name="userlist"),
    path('userlist/<str:pk>/',UserDetailAV.as_view(), name="userdetail"),
    
    path('banklist/', BankListAV.as_view(), name="banklist"),
    path('banklist/<str:pk>/', BankDetailAV.as_view(), name="bankdetail"),
    
    path('takalist/', TakaListAV.as_view(), name="takalist"),
    path('takalist/<str:pk>/', TakaDetailAV.as_view(), name="takadetail"),
]