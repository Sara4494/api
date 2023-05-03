from django.urls import path,include
from app.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
routrr= DefaultRouter()
routrr.register('guests',viewsets_guest)
routrr.register('movies',viewsets_Movie)
routrr.register('reservations',Reservation_Movie)

urlpatterns = [
    path('',no_rest_no_model,name= 'no_rest_no_model'),
    path('no_rest_from_models/',no_rest_from_models,name= 'no_rest_from_models'),
    path('fbv_list/',FBV_List,name= 'FBV_List'),
    path('fbv_list/FBV_pk/<int:pk>/',FBV_pk,name= 'FBV_pk'),
    path('fbv_list/',FBV_List,name= 'FBV_List'),
    path('rest/cbv/',CBV_List.as_view(),name= 'CBV_List'),
    path('CBV_pk/<int:pk>/',CBV_pk.as_view(),name= 'CBV_pk'),
    path('fbv_list/',FBV_List,name= 'FBV_List'),
    path('Mixins_list',Mixins_list.as_view(),name= 'Mixins_list'),
    
     
    path('mixin_pk/<int:pk>/',mixin_pk.as_view(),name= 'mixin_pk'),
    path('Generics_list',Generics_list.as_view(),name= 'Generics_list'),
    path('Generics_pk/<int:pk>/',Generics_pk.as_view(),name= 'Generics_pk'),
    path('Generics_list/',include(routrr.urls)),#erics_list/guests/3/
    path('find_movie/',find_movie,name= 'find_movie'),
    path('new_reservation/',new_reservation,name= 'new_reservation'),
    #rest auth urls
    path('api-auth',include('rest_framework.urls')),
    
    #Token authetication
   # python manage.py migrate
    path('api-token',obtain_auth_token),
     #python manage.py migrate
    
    path('Post_pk/<int:pk>/',Post_pk.as_view(),name= 'Post_pk'),
    
     
    ]
      
    
