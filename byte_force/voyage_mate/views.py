import json

from django.shortcuts import render
from django.views import View

from .models import TagPhrase

# Create your views here.
class IndexView(View):
    def get(self, request):

        phrases = json.load(open("voyage_mate/tag_phrases.json"))
        print(phrases["IN"])

        
        return render(request, 'voyage_mate/index.html')