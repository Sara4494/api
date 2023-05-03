from django.db import models
from rest_framework.authtoken.models import Token
from django.core.validators import MaxValueValidator ,MinValueValidator

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User
 

# Create your models here.
# Guest -- Movie --Reservation
class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie =models.CharField(max_length=10)
    date = models.DateField()



class Juest(models.Model):
    name = models.CharField(max_length=30)
    mobil = models.CharField(max_length=20)
    
class Reservation(models.Model):
    guest = models.ForeignKey(Juest,related_name='reservation',on_delete=models.CASCADE)
    movie  = models.ForeignKey(Movie,related_name='reservation',on_delete=models.CASCADE)
class Post (models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50 ,blank=True ,null=True)
    body = models.TextField(blank=True,null=True)
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
####################################################################
#uuid
           
class Meal(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=350)

    def __str__(self):
        return self.title
class Rating(models.Model):
    meal =models.ForeignKey(Meal,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    #def __str__(self):
     #   return self.meal
    class Mets:
        unique_together  = (('user','meal'))
        index_together  =(('user','meal'))
