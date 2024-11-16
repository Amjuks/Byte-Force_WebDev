from django.contrib import admin


# Register your models here.
from .models import Destination
from .models import Review
from .models import Itinerary
from .models import TagPhrase
from .models import Notification
from .models import Message


admin.site.register(Destination) 
admin.site.register(Review)
admin.site.register(Itinerary)
admin.site.register(TagPhrase)
admin.site.register(Notification)
admin.site.register(Message)





