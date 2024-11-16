from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse

from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url="voyage_mate/", permanent=False)),
    path('voyage_mate/', include('voyage_mate.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)