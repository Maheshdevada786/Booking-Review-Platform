from django import forms
from .models import Hotel, Restaurant, Mall, Booking, Review    

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'description', 'image', 'review_score']


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'image', 'review_score']

class MallForm(forms.ModelForm):
    class Meta:
        model = Mall
        fields = ['name', 'description', 'image', 'review_score']        


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'category', 'date', 'status']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'category', 'comment', 'rating']

