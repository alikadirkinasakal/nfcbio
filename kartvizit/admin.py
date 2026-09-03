from django.contrib import admin
from .models import (
    Musteri, MusteriTelefon, MusteriWhatsapp, 
    MusteriEmail, MusteriInstagram, MusteriFacebook, 
    MusteriGoogleMaps, MusteriIban
)

class TelefonInline(admin.TabularInline):
    model = MusteriTelefon
    extra = 6

class WhatsappInline(admin.TabularInline):
    model = MusteriWhatsapp
    extra = 6

class EmailInline(admin.TabularInline):
    model = MusteriEmail
    extra = 1

class InstagramInline(admin.TabularInline):
    model = MusteriInstagram
    extra = 1

class FacebookInline(admin.TabularInline):
    model = MusteriFacebook
    extra = 1

class GoogleMapsInline(admin.TabularInline):
    model = MusteriGoogleMaps
    extra = 1

class IbanInline(admin.TabularInline):
    model = MusteriIban
    extra = 5

@admin.register(Musteri)
class MusteriAdmin(admin.ModelAdmin):
    list_display = ('ad_soyad', 'unvan', 'url_slug')
    inlines = [
        TelefonInline, 
        WhatsappInline, 
        EmailInline, 
        InstagramInline, 
        FacebookInline, 
        GoogleMapsInline, 
        IbanInline
    ]