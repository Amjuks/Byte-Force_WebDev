import os
import json
import openai

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from .models import TagPhrase

from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_client = openai.OpenAI(api_key=openai_api_key)



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
    
class IternaryFormView(View):
    def get(self, request):
        return render(request, 'voyage_mate/itinerary-form.html')

    def post(self, request):
        data = {
            "Which country do you want to travel?": request.POST.get('country', ''),
            "How many days are you planning to travel?": request.POST.get('days', ''),
            "What is your budget?": request.POST.get('budget', ''),
            "What are your interests in travelling?": request.POST.get('interests', ''),
            "Travelling with:": request.POST.get('companions', ''),
            "Preferred Accommodation Type": request.POST.get('accommodation', ''),
            "Preferred Travel Season": request.POST.get('season', ''),
            "Preferred Activity Level": request.POST.get('activity', ''),
            "Dietary Preferences/Restrictions": request.POST.get('diet', ''),
            "Preferred Mode of Transportation": request.POST.get('transport', ''),
        }
        
        info = "\n\n".join(f"{key}\n{value}" for key, value in data.items() if value)
        # For debugging or testing purposes
        print(info)

        return redirect(reverse("voyage_mate:itinerary"))

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