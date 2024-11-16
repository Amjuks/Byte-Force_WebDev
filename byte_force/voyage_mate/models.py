import json

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    place = models.CharField(max_length=255)
    description= models.TextField()
    image_url=models.URLField()

    def __str__(self):
        return self.place 
    
class Review(models.Model):
    destination = models.ForeignKey(Destination, related_name='reviews', on_delete=models.CASCADE)  # Links to the destination being reviewed
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to the user who wrote the review
    rating = models.IntegerField()  # Rating given to the destination (1-5)
    text = models.TextField()  # The actual review text
    created_at = models.DateTimeField(auto_now_add=True)  # set the date/time of  when the review was created

    def __str__(self):
        return f'Review by {self.user.username} for {self.destination.name}'  # display of the review
    
class Itinerary(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)  
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)  # Reference to Destination model
    num_days = models.IntegerField()  
    itinerary_details = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Itinerary for {self.destination.name} ({self.num_days} days)"

class TagPhrase(models.Model):
    country = models.CharField(max_length=10)
    phrase = models.CharField(max_length=100)  

    @classmethod
    def update_phrases(cls):
        phrases = json.load(open('voyage_mate/tag_phrases.json'))

        cls.objects.all().delete()

        for country, phrase in phrases:
            cls.objects.create(country=country, phrase=phrase).save()

    def __str__(self):
        return f"{self.phrase} for {self.country}"
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')  
    message = models.TextField()  
    read = models.BooleanField(default=False)  # Whether the user has read the message or not
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the notification was created

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:20]}..."  # Display part of the message
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    message = models.TextField()
    country = models.CharField(max_length=200)


    def __str__(self):
        return f"Message from {self.user.username} in {self.country}"
    
class City(models.Model):
    place = models.CharField(max_length=255)
    description= models.TextField()
    image_url=models.URLField()

    def __str__(self):
        return self.place 
    

class Connector(models.Model):
    country = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='connectors')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='connectors')

    def __str__(self):
        return f"Connector: {self.country.place} - {self.city.place}"
    
    
    
    