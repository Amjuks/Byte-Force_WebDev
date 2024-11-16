from django.contrib import admin


# Register your models here.
from .models import Destination, Review, Itinerary, TagPhrase, Notification, Message, City, Connector


admin.site.register(Destination) 
admin.site.register(Review)
admin.site.register(Itinerary)
admin.site.register(TagPhrase)
admin.site.register(Notification)
admin.site.register(Message)
admin.site.register(City)
admin.site.register(Connector)








