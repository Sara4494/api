from rest_framework import serializers
from app.models import *
class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields ='__all__'
        
class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields ='__all__'
        
class GuestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Juest
        fields = ['pk','reservation','name','mobil']
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =  '__all__'
#uuid
#######################################################
class MealSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id','title','description']
class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','meal','user','stars'] 
        