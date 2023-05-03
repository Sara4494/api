from django.shortcuts import render
from django.http.response import JsonResponse  
from app.models import *
from rest_framework.decorators import api_view
from app.serializers import *
from rest_framework import status,filters  
from rest_framework.views import APIView
 
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics ,mixins ,viewsets
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from app.permissions import *
#5GmuEKiCUF8QwzR
#1 without REST and no modil query FBV
def no_rest_no_model(request):
    guests = [
        {'id': 1 ,
         'Name':'Omar',
         'mobile':4567,
         },
         {'id': 2 ,
         'Name':'yassin',
         'mobile':9787,
         }
        
    ]
    return JsonResponse (guests,safe= False)

#2 model data default django without rest
def no_rest_from_models(request):
    data = Juest.objects.all()
    response ={
        'guests': list(data.values('name','mobil'))
    }
    return JsonResponse (response)
    

# 3 List ==GET 
# Create ==POSt
#pk query ==GEt
# Update == PUT
#Delete destroy ==DELETE
#Function based views
#3.1 GET POSt
@api_view(['GET','POSt'])
def FBV_List(request):
    #GET
    if request.method == 'GET':
        guests = Juest.objects.all()
        serializer = GuestSerializers(guests ,many =True)
        return Response(serializer.data)
    
        
    #POST
    elif request.method == 'POST':
         
        serializer = GuestSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data ,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
        

#3.1 GET PUT DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def FBV_pk(request,pk):
    try:
       guest  = Juest.objects.get(pk=pk)
    except Juest.DoesNotExists:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    #GET
    if request.method == 'GET':
        serializer = GuestSerializers(guest)
        return Response(serializer.data)
    
        
    #PUT
    elif request.method == 'PUT':
         
        serializer = GuestSerializers(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    if request.method == 'DELETE':
    
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#CBV class based views
#4.1 List and Create == GET and POST
class CBV_List(APIView):
    def get(self, request):
        guests = Juest.objects.all()
        serializer = GuestSerializers(guests,many =True)
        return Response(serializer.data)
    def post(self, request):
       
        serializer = GuestSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.data ,status=status.HTTP_400_BAD_REQUEST)
        
    
#4.2 GET PUT DELETE class based views -- pk a
class CBV_pk(APIView):
    def get_object(self, pk):
        try:
            return Juest.objects.get(pk=pk)
        except  Juest.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        guests = self.get_object(pk)
        serializer = GuestSerializers(guests)
        return Response(serializer.data)
    def put(self, request,pk):
        guests = self.get_object(pk)
       
        serializer = GuestSerializers(guests,data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data )
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        guests = self.get_object(pk)
        guests.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
#5 Mixins
#5.1 mixins list
class Mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Juest.objects.all()
    serializer_class =GuestSerializers
    def get(self ,request):
        return self.list(request)
    def post(self ,request):
        return self.create(request)
#5.2 mixins get put delete
class mixin_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Juest.objects.all()
    serializer_class =GuestSerializers
    def get(self ,request,pk):
        return self.retrieve(request)
    def put(self ,request,pk):
        return self.update(request)
    def delete(self ,request,pk):
        return self.destroy(request)

#6 Generics
#6.1 get and post
class Generics_list(generics.ListCreateAPIView):
    queryset = Juest.objects.all()
    serializer_class =GuestSerializers
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

#6.2 get and put and delete
class Generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Juest.objects.all()
    serializer_class =GuestSerializers
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    
# 7 viewsets
class viewsets_guest(viewsets.ModelViewSet):
    queryset = Juest.objects.all()
    serializer_class =GuestSerializers


class viewsets_Movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class =MovieSerializers
    filter_backends =[filters.SearchFilter]
    search_fields = ['movie']
    
class Reservation_Movie(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers

#8 Find movie
@api_view(['GET'])
def find_movie(request):
    movies = Movie.objects.filter(  
        movie= request.data['movie'],
        hall =request.data['hall'], 
    )
    serializer = MovieSerializers( movies ,many = True)
    return Response(serializer.data)
#9 create new reservation
@api_view(['POST'])
def new_reservation(request):
    movie = Movie.objects.get(  
        movie= request.data['movie'],
        hall =request.data['hall'], 
    )
    guest =Juest()
    guest.name =request.data['name']
    guest.name =request.data['mobil']
    guest.save()
    
    serializer = Reservation()
    serializer.guest =guest
    serializer.movie=movie
    serializer.save()
    
    return Response(status=status.HTTP_201_CREATED)
#10 post author editor
class Post_pk(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthorOreadOnly]
  queryset = Post.objects.all()
  serializer_class = PostSerializer
