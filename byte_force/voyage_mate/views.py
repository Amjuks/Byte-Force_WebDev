import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import TagPhrase

# Create your views here.
class IndexView(View):
    def get(self, request):


        print(TagPhrase.objects.get(country="IN"))
        return render(request, 'voyage_mate/index.html')
    

class TagPhraseAPIView(View):
    def get(self, request, country: str):
        
        phrase = TagPhrase.objects.get(country=country).phrase
        return JsonResponse({'phrase': phrase})