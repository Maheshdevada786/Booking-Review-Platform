
from django.shortcuts import render,  redirect, get_object_or_404
from .models import Hotel, Restaurant, Mall, Booking, Review
from .forms import HotelForm, RestaurantForm, MallForm, BookingForm, ReviewForm  


def home(request):
    return render(request, 'home.html')


def hotels(request):
    hotels = Hotel.objects.all()

    # search functionality
    search_query = request.GET.get("search")
    if search_query:
        hotels = hotels.filter(name__icontains=search_query)

    # rating filter
    rating_value = request.GET.get("rating")
    if rating_value:
        hotels = hotels.filter(review_score__gte=rating_value)
    return render(request, 'hotels.html', {'hotels': hotels})

def add_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:hotels')
    else:
        form = HotelForm()
    return render(request, 'hotel_form.html', {'form': form, 'action': 'Add Hotel'})

def update_hotel(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('myapp:hotels')
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'hotel_form.html', {'form': form, 'action': 'Update Hotel'})

def delete_hotel(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        hotel.delete()
        return redirect('myapp:hotels')
    return render(request, 'hotel_confirm_delete.html', {'hotel': hotel})



def malls(request):
    malls = Mall.objects.all()

    # search functionality
    search_query = request.GET.get("search")
    if search_query:
        malls = malls.filter(name__icontains=search_query)

    # rating filter
    rating_value = request.GET.get("rating")
    if rating_value:
        malls = malls.filter(review_score__gte=rating_value) 
    return render(request, 'malls.html', {'malls': malls})

def add_mall(request):
    if request.method == 'POST':
        form = MallForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:malls')
    else:
        form = MallForm()
    return render(request, 'mall_form.html', {'form': form, 'action': 'Add Mall'})

def update_mall(request, pk):
    mall = get_object_or_404(Mall, pk=pk)
    if request.method == 'POST':
        form = MallForm(request.POST, request.FILES, instance=mall)
        if form.is_valid():
            form.save()
            return redirect('myapp:malls')
    else:
        form = MallForm(instance=mall)
    return render(request, 'mall_form.html', {'form': form, 'action': 'Update Mall'})

def delete_mall(request, pk):
    mall = get_object_or_404(Mall, pk=pk)
    if request.method == 'POST':
        mall.delete()
        return redirect('myapp:malls')
    return render(request, 'mall_confirm_delete.html', {'mall': mall})



def restaurants(request):
    restaurants = Restaurant.objects.all()

    # search functionality
    search_query = request.GET.get("search")
    if search_query:
        restaurants = restaurants.filter(name__icontains=search_query)

    # rating filter
    rating_value = request.GET.get("rating")
    if rating_value:
        restaurants = restaurants.filter(review_score__gte=rating_value) 
    return render(request, 'restaurants.html', {'restaurants': restaurants})    

def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:restaurants')
    else:
        form = RestaurantForm()
    return render(request, 'restaurant_form.html', {'form': form, 'action': 'Add Restaurant'})

def update_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('myapp:restaurants')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurant_form.html', {'form': form, 'action': 'Update Restaurant'})

def delete_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('myapp:restaurants')
    return render(request, 'restaurant_confirm_delete.html', {'restaurant': restaurant})



def bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings.html', {'bookings': bookings})

def booking_create(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('myapp:bookings')
    return render(request, 'booking_form_fixed.html', {'form': form, 'title': 'Add Booking'})

def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    form = BookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        form.save()
        return redirect('myapp:bookings')
    return render(request, 'booking_form_fixed.html', {'form': form, 'title': 'Update Booking'})

def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('myapp:bookings')
    return render(request, 'booking_delete.html', {'booking': booking})



def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})

def review_create(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('myapp:reviews')
    return render(request, 'review_form.html', {'form': form, 'title': 'Add Review'})

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('myapp:reviews')
    return render(request, 'review_form.html', {'form': form, 'title': 'Update Review'})

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('myapp:reviews')
    return render(request, 'review_delete.html', {'review': review})


def about(request):
    return render(request, 'about.html')