from django.shortcuts import render, get_object_or_404
from .models import Musteri

def profil_goruntule(request, slug):
    # Linkteki uzantıya (slug) sahip müşteriyi bulur
    musteri = get_object_or_404(Musteri, url_slug=slug)
    
    # Müşteri verilerini 'profil.html' sayfasına gönderir
    return render(request, 'kartvizit/profil.html', {'musteri': musteri})