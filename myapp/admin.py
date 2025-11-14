
from django.contrib import admin
from .models import Hotel, Restaurant, Mall, Booking, Review


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'review_score')
    search_fields = ('name',)
    list_filter = ('review_score',)

admin.site.register(Hotel, HotelAdmin)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'review_score')
    search_fields = ('name',)
    list_filter = ('review_score',)

@admin.register(Mall)
class MallAdmin(admin.ModelAdmin):  
    list_display = ('name', 'review_score')
    search_fields = ('name',)
    list_filter = ('review_score',) 

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date', 'status')
    list_filter = ('category', 'status')
    search_fields = ('name', 'category')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rating')
    list_filter = ('category', 'rating')
    search_fields = ('name', 'category')


        
