from django.contrib import admin
from .models import (
    Musteri, MusteriTelefon, MusteriKampanya, MusteriWhatsapp, 
    MusteriEmail, MusteriInstagram, MusteriTikTok, MusteriSnapchat, MusteriWebsite, 
    MusteriSahibinden, MusteriFacebook, 
    MusteriGoogleMaps, MusteriIban, 
)

class TelefonInline(admin.TabularInline):
    model = MusteriTelefon
    extra = 6

class MusteriKampanyaInline(admin.TabularInline):
    model = MusteriKampanya
    extra = 2

class WhatsappInline(admin.TabularInline):
    model = MusteriWhatsapp
    extra = 6

class EmailInline(admin.TabularInline):
    model = MusteriEmail
    extra = 1

class InstagramInline(admin.TabularInline):
    model = MusteriInstagram
    extra = 1

class MusteriTikTokInline(admin.TabularInline):
    model = MusteriTikTok
    extra = 1

class MusteriSnapchatInline(admin.TabularInline):
    model = MusteriSnapchat
    extra = 1

class MusteriWebsiteInline(admin.TabularInline):
    model = MusteriWebsite
    extra = 1

class MusteriSahibindenInline(admin.TabularInline):
    model = MusteriSahibinden
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
        MusteriKampanyaInline, 
        WhatsappInline, 
        EmailInline, 
        InstagramInline,
        MusteriTikTokInline, 
        MusteriSnapchatInline, 
        MusteriWebsiteInline, 
        MusteriSahibindenInline,
        FacebookInline, 
        GoogleMapsInline, 
        IbanInline
    ]