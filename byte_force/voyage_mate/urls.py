from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.IndexView.as_view(), name='index'),
    path('register/', views.IndexView.as_view(), name='index'),
    
    path('', views.IndexView.as_view(), name='index'),
    path('phrase/<str:country>', views.TagPhraseAPIView.as_view(), name='phrase')
]