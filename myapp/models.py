from email import message
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone



# Create your models here.

class Profile(models.Model):

    position = [
        ("Personal" , "Personal"),
        ("Business" , "Business"),
        ("Retirement" , "Retirement"),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    account_type = models.CharField(max_length=10, null=True, choices=position, default="Personal")
    phone_number = models.CharField(unique=False, max_length=100, null=True)
    balance = models.PositiveIntegerField(default=0)
    wallet = models.CharField(max_length=64,blank=True, default='12345667788')

    @receiver(post_save, sender= User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        
    @receiver(post_save, sender= User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self) -> str:
        return self.user.id
    
class withdrawal_table(models.Model):
    withdrawal_id = models.AutoField(primary_key=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    amount = models.PositiveIntegerField()
    comments = models.CharField(max_length=40, default='Unconfirmed')
    status = models.CharField(max_length=10, default='Pending')
    withdrawal_account = models.CharField(max_length=40)
    withdrawal_wallet = models.CharField(max_length=40)
    date_generated = models.DateTimeField(default=timezone.now)

class deposits_table(models.Model):
    deposit_id = models.AutoField(primary_key=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    amount = models.PositiveIntegerField()
    comments = models.CharField(max_length=40, default='Unconfirmed')
    status = models.CharField(max_length=10, default='Pending')
    date_generated = models.DateTimeField(default=timezone.now)

class notifications_table(models.Model):
    notification_id = models.AutoField(primary_key=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    type = models.CharField(max_length=16)
    message = models.TextField()
    date_generated = models.DateTimeField(default=timezone.now)

class wallet_table(models.Model):
    wallet_id = models.AutoField(primary_key=True, blank=True)
    wallet_address = models.CharField(max_length=80)
    wallet_coin = models.CharField(max_length=16)

class history_table(models.Model):
    history_id = models.AutoField(primary_key=True, blank=True)
    history_address = models.CharField(max_length=80)
    history_coin = models.CharField(max_length=16)