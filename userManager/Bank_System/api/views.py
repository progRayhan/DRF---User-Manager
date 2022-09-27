from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userProfile_app.models import UserProfile
from userProfile_app.api.serializers import UserProfileSerializer
from Bank_System.models import Bank, Taka
from Bank_System.api.serializers import BankSerializer, TakaSerializer

class UserListAV(APIView):
    def get(self, request):
        userName = UserProfile.objects.all()
        serializer = UserProfileSerializer(userName, many=True)
        return Response(serializer.data)
    
class UserDetailAV(APIView):
    def get(self, request, pk):
        try:
            userName = UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            return Response({'errors': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(userName)
        return Response(serializer.data)
    


class BankListAV(APIView):
    def get(self, request):
        bank = Bank.objects.all()
        serializer = BankSerializer(bank, many=True)
        return Response(serializer.data)
    
class BankDetailAV(APIView):
    def get(self, request, pk):
        try:
            bank = Bank.objects.get(pk=pk)
        except Bank.DoesNotExist:
            return Response({'errors' : 'Bank not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BankSerializer(bank)
        return Response(serializer.data)
    


class TakaListAV(APIView):
    def get(self, request):
        taka = Taka.objects.all()
        serializer = TakaSerializer(taka, many=True)
        return Response(serializer.data)
    
class TakaDetailAV(APIView):
    def get(self, request, pk):
        try:
            taka = Taka.objects.get(pk=pk)
        except Taka.DoesNotExist:
            return Response({'errors' : 'Taka does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TakaSerializer(taka)
        return Response(serializer.data)