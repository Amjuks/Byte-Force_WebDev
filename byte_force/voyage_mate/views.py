import os
import json
import openai

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from .models import ChatRoom, ChatMessage

from .models import TagPhrase, Itinerary, City, Review

from dotenv import load_dotenv
from voyage_mate.travel_schema import TRAVEL_ITINERARY_SCHEMA, TRAVEL_PROMPT

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_client = openai.OpenAI(api_key=openai_api_key)



# Create your views here.
class IndexView(View):
    def get(self, request):
        context = {}
        context['cities'] = City.objects.all().order_by('?')[:9]
        context['reviews'] = Review.objects.all().order_by('?')[:3]
        return render(request, 'voyage_mate/index.html', context)
    
class TagPhraseAPIView(View):
    def get(self, request, country: str):
        phrase = TagPhrase.objects.get(country=country).phrase
        return JsonResponse({'phrase': phrase})

class AboutView(View):
    def get(self, request):
        return render(request, 'voyage_mate/about.html')
    

class ReviewView(View):
    def post(self, request, city_id: int):
        city = get_object_or_404(City, id=city_id)
        text = request.POST.get('experience')

        if text:
            Review.objects.create(
                destination=city,
                user=request.user,
                text=text
            )

            return redirect(reverse('voyage_mate:city', args=[city_id]))
        
        return redirect(reverse('voyage_mate:city', args=[city_id]))


class IternaryFormView(View):
    def get(self, request):
        context = {}
        context['cities'] = [city.place for city in City.objects.all()]
        return render(request, 'voyage_mate/itinerary-form.html', context)

    def post(self, request):
        context = {}
        data = {
            "Where do you want to travel?": request.POST.get('destination', ''),
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
        info = TRAVEL_PROMPT.format(info)

        response = openai_client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            response_format=TRAVEL_ITINERARY_SCHEMA,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": info
                        },
                    ]
                }
            ]
        )

        
        context['info'] = json.loads(response.choices[0].message.content)
        destination = context['info']['destination']
        num_days = context['info']['number_of_days']
        try:
            details = '\n\n'.join(day for day in context['info']['itinerary'])
        except:
            details = '\n\n'.join(day for day in context['info']['itinerary'].values())

        Itinerary.objects.create(
            user=request.user,
            destination=destination,
            num_days=num_days,
            itinerary_details=details,
        ).save()

        return render(request, 'voyage_mate/itinerary.html', context)

class CityView(View):
    def get(self, request, city_id: int):
        context = {}
        context['city'] = City.objects.get(id=city_id)
        context['reviews'] = Review.objects.filter(destination=context['city']).order_by('?')[:3]
        return render(request, 'voyage_mate/city.html', context)    

class NotificationView(View):
    def get(self, request):
        return render(request, 'voyage_mate/notifications.html')
    
    def post(self, request):
        ...

class ChatView(View):
    def get(self, request):
        return render(request, 'voyage_mate/chat.html')
    
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