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

# Bütün alanlar için artı (+) butonuna basılarak çoğaltılabilen esnek model
class MusteriLink(models.Model):
    TUR_SECENEKLERI = (
        ('telefon', 'Telefon'),
        ('whatsapp', 'WhatsApp'),
        ('email', 'E-Posta'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('google_maps', 'Google Maps'),
        ('iban', 'IBAN'),
    )

    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='linkler')
    tur = models.CharField(max_length=20, choices=TUR_SECENEKLERI, verbose_name="Alan Türü")
    deger = models.CharField(max_length=255, verbose_name="Değer / Numara / Link")

    def __str__(self):
        return f"{self.get_tur_display()} - {self.deger}"