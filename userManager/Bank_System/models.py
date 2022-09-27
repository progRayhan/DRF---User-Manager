from django.db import models
from userProfile_app.models import UserProfile

# Create your models here.
BANK_CHOICES = (
    ('sonali', 'Sonali'),
    ('rupali', 'Rupali'),
    ('agrani', 'Agrani'),
    ('janata', 'Janata'),
    ('brac', 'BRAC'),
    ('ific', 'IFIC'),
    ('one', 'One'),
    ('dutch', 'Dutch'),
)
        
class Bank(models.Model):
    """Bank model"""
    bank_name = models.CharField(max_length=6, choices=BANK_CHOICES, default='sonali')
    
    def __str__(self):
        return self.bank_name
    


class Taka(models.Model):
     """Taka model"""
     balance = models.CharField(max_length=10)
     userName = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
     bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
     
     def __str__(self):
         return f'{self.userName} - {self.balance} - {self.bank}'