from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    place = models.CharField(max_length=255)
    description= models.TextField(max_length=255)
    image_url=models.URLField()

    def __str__(self):
        return self.name 
    
class Review(models.Model):
    destination = models.ForeignKey(Destination, related_name='reviews', on_delete=models.CASCADE)  # Links to the destination being reviewed
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to the user who wrote the review
    rating = models.IntegerField()  # Rating given to the destination (1-5)
    text = models.TextField()  # The actual review text
    created_at = models.DateTimeField(auto_now_add=True)  # set the date/time of  when the review was created

    def __str__(self):
        return f'Review by {self.user.username} for {self.destination.name}'  # display of the review