from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from kartvizit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Eğer linke bir isim girilirse (örn: /ali-kadir) views.py'deki fonksiyona git
    path('<slug:slug>/', views.profil_goruntule, name='profil'),
]

# Fotoğrafların tarayıcıda yüklenebilmesi için gereken ayar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)