from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    path('', views.IndexView.as_view(), name='index'),
    path('phrase/<str:country>', views.TagPhraseAPIView.as_view(), name='phrase')
]