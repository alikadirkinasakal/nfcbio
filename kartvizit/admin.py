from django.contrib import admin
from .models import Musteri, MusteriLink

class MusteriLinkInline(admin.TabularInline):
    model = MusteriLink
    extra = 1  # Her seferinde 1 boş satır ve ekleme butonu getirir

@admin.register(Musteri)
class MusteriAdmin(admin.ModelAdmin):
    list_display = ('ad_soyad', 'unvan', 'url_slug')
    inlines = [MusteriLinkInline]