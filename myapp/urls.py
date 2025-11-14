from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('hotels/', views.hotels, name='hotels'), 
    path('hoteladd/', views.add_hotel, name='add_hotel'),
    path('hotelupdate/<int:pk>/', views.update_hotel, name='update_hotel'),
    path('hoteldelete/<int:pk>/', views.delete_hotel, name='delete_hotel'), 

    path('malls/', views.malls, name='malls'),
    path('malladd/', views.add_mall, name='add_mall'),
    path('mallupdate/<int:pk>/', views.update_mall, name='update_mall'),
    path('malldelete/<int:pk>/', views.delete_mall, name='delete_mall'),

    path('restaurants/', views.restaurants, name='restaurants'),
    path('restaurantadd/', views.add_restaurant, name='add_restaurant'),
    path('restaurantupdate/<int:pk>/', views.update_restaurant, name='update_restaurant'),
    path('restaurantdelete/<int:pk>/', views.delete_restaurant, name='delete_restaurant'),


    path('reviews/', views.reviews, name='reviews'),
    path('reviewcreate/', views.review_create, name='review_create'),
    path('reviewupdate/<int:pk>/', views.review_update, name='review_update'),
    path('reviewdelete/<int:pk>/', views.review_delete, name='review_delete'),

    path('bookings/', views.bookings, name='bookings'),
    path('bookingcreate/', views.booking_create, name='booking_create'),
    path('bookingupdate/<int:pk>/', views.booking_update, name='booking_update'),
    path('bookingdelete/<int:pk>/', views.booking_delete, name='booking_delete'),
    
    path('about/', views.about, name='about'),


    
]
app_name = 'myapp'
