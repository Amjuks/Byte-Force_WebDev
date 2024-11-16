from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('phrase/<str:country>', views.TagPhraseAPIView.as_view(), name='phrase')
]