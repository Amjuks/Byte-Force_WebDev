from django.urls import path

from . import views

app_name = "voyage_mate"

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    path('', views.IndexView.as_view(), name='index'),
    path('phrase/<str:country>', views.TagPhraseAPIView.as_view(), name='phrase')
]