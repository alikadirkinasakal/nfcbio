from django.db import models
from PIL import Image

class Musteri(models.Model):
    ad_soyad = models.CharField(max_length=100, verbose_name="Ad Soyad")
    unvan = models.CharField(max_length=100, verbose_name="Ünvan", blank=True, null=True)
    url_slug = models.SlugField(unique=True, verbose_name="URL Uzantısı (Örn: ali-kadir)")
    
    profil_fotografi = models.ImageField(upload_to='profiller/', verbose_name="Profil Fotoğrafı")
    
    telefon = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefon")
    whatsapp = models.CharField(max_length=20, blank=True, null=True, verbose_name="WhatsApp")
    email = models.EmailField(blank=True, null=True, verbose_name="E-Posta")
    instagram = models.URLField(blank=True, null=True, verbose_name="Instagram")
    facebook = models.URLField(blank=True, null=True, verbose_name="Facebook")
    google_maps = models.URLField(blank=True, null=True, verbose_name="Google Maps")
    iban = models.CharField(max_length=50, blank=True, null=True, verbose_name="IBAN")

    def __str__(self):
        return self.ad_soyad

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.profil_fotografi:
            img = Image.open(self.profil_fotografi.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.profil_fotografi.path, quality=85)