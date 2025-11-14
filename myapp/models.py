
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='imagesData/')
    review_score = models.DecimalField(max_digits=3, decimal_places=1)  # e.g. 4.5

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='imagesData/')
    review_score = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name
    
class Mall(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='imagesData/')
    review_score = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name    


class Booking(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[('Hotel', 'Hotel'), ('Restaurant', 'Restaurant'), ('Mall', 'Mall')])
    date = models.DateField()
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.name} - {self.category}"


class Review(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[('Hotel', 'Hotel'), ('Restaurant', 'Restaurant'), ('Mall', 'Mall')])
    comment = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f"{self.name} - {self.rating}"    
