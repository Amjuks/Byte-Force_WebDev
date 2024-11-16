from django.urls import path

from . import views

app_name = "voyage_mate"

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('about/', views.AboutView.as_view(), name='about'),
    
    path('itinerary/', views.IternaryFormView.as_view(), name='itinerary'),
    path('notification/', views.NotificationView.as_view(), name='notification'),

    path('', views.IndexView.as_view(), name='index'),
    path('phrase/<str:country>', views.TagPhraseAPIView.as_view(), name='phrase')
]