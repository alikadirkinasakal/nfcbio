from django.db import models
from PIL import Image

class Musteri(models.Model):
    ad_soyad = models.CharField(max_length=100, verbose_name="Ad Soyad")
    unvan = models.CharField(max_length=100, verbose_name="Ünvan", blank=True, null=True)
    url_slug = models.SlugField(unique=True, verbose_name="URL Uzantısı (Örn: ali-kadir)")
    profil_fotografi = models.ImageField(upload_to='profiller/', verbose_name="Profil Fotoğrafı")

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

# Tüm alt modellerin değer (deger/numara/link) alanlarına blank=True, null=True ekliyoruz
class MusteriTelefon(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='telefonlar')
    telefon = models.CharField(max_length=20, verbose_name="Telefon Numarası", blank=True, null=True)

class MusteriWhatsapp(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='whatsapplar')
    whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp Numarası", blank=True, null=True)

class MusteriEmail(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='emailler')
    email = models.EmailField(verbose_name="E-Posta Adresi", blank=True, null=True)

class MusteriInstagram(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='instagramlar')
    instagram = models.URLField(verbose_name="Instagram Profil Linki", blank=True, null=True)

class MusteriFacebook(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='facebooklar')
    facebook = models.URLField(verbose_name="Facebook Profil Linki", blank=True, null=True)

class MusteriGoogleMaps(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='haritalar')
    google_maps = models.URLField(verbose_name="Google Maps Konum Linki", blank=True, null=True)

class MusteriIban(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='ibanlar')
    iban = models.CharField(max_length=50, verbose_name="IBAN Numarası", blank=True, null=True)