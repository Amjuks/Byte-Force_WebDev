import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from .models import ChatRoom, ChatMessage

from .models import TagPhrase

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'voyage_mate/index.html')
    
class TagPhraseAPIView(View):
    def get(self, request, country: str):
        phrase = TagPhrase.objects.get(country=country).phrase
        return JsonResponse({'phrase': phrase})

class AboutView(View):
    def get(self, request):
        return render(request, 'voyage_mate/about.html')
    
class IternaryForm(View):
    def get(self, request):
        return render(request, 'voyage_mate/itinerary-form.html')

class NotificationView(View):
    def get(self, request):
        return render(request, 'voyage_mate/notifications.html')

class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'voyage_mate/sign-in.html')
    
    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("voyage_mate:index"))
        else:
            return render(request, "voyage_mate/sign-in.html", {
                "message": "Invalid username and/or password."
            })

class RegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'voyage_mate/register.html')
    
    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST["username"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "voyage_mate/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "voyage_mate/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("voyage_mate:index"))

class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return HttpResponseRedirect(reverse("voyage_mate:index"))
    
def chat_room(request, room_name):
    room, created = ChatRoom.objects.get_or_create(name=room_name)
    messages = ChatMessage.objects.filter(room=room).order_by('-timestamp')[:10]
    return render(request, 'chat_room.html', {
        'room_name': room_name,
        'messages': messages
    })