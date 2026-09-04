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

class MusteriKampanya(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='kampanyalar')
    metin = models.CharField(max_length=255, verbose_name="Kampanya / Duyuru Metni", blank=True, null=True)

    def __str__(self):
        return f"{self.musteri.ad_soyad} - {self.metin}"
   
class MusteriWhatsapp(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='whatsapplar')
    whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp Numarası", blank=True, null=True)

class MusteriEmail(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='emailler')
    email = models.EmailField(verbose_name="E-Posta Adresi", blank=True, null=True)

class MusteriInstagram(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='instagramlar')
    instagram = models.CharField(max_length=255, verbose_name="Instagram Kullanıcı Adı veya Linki", blank=True, null=True)

    def get_url(self):
        if not self.instagram:
            return "#"
        val = self.instagram.strip()
        if val.startswith('http://') or val.startswith('https://'):
            return val
        return f"https://instagram.com/{val.lstrip('@')}"
    
class MusteriTikTok(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='tiktoklar')
    tiktok = models.CharField(max_length=255, verbose_name="TikTok Kullanıcı Adı veya Linki", blank=True, null=True)

    def get_url(self):
        if not self.tiktok:
            return "#"
        val = self.tiktok.strip()
        if val.startswith('http://') or val.startswith('https://'):
            return val
        return f"https://tiktok.com/@{val.lstrip('@')}"

class MusteriSnapchat(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='snapchatler')
    snapchat = models.CharField(max_length=255, verbose_name="Snapchat Kullanıcı Adı veya Linki", blank=True, null=True)

    def get_url(self):
        if not self.snapchat:
            return "#"
        val = self.snapchat.strip()
        if val.startswith('http://') or val.startswith('https://'):
            return val
        return f"https://www.snapchat.com/add/{val.lstrip('@')}"
    
class MusteriWebsite(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='websiteler')
    website = models.CharField(max_length=255, verbose_name="Web Sitesi Linki", blank=True, null=True)

    def get_url(self):
        if not self.website:
            return "#"
        val = self.website.strip()
        if val.startswith('http://') or val.startswith('https://'):
            return val
        return f"https://{val}"

    def __str__(self):
        return f"{self.musteri.ad_soyad} - Web: {self.website}"
    
class MusteriSahibinden(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='sahibindenler')
    sahibinden = models.CharField(max_length=255, verbose_name="Sahibinden Mağaza/Profil Linki veya Kullanıcı Adı", blank=True, null=True)

    def get_url(self):
        if not self.sahibinden:
            return "#"
        val = self.sahibinden.strip()
        if val.startswith('http://') or val.startswith('https://'):
            return val
        return f"https://www.sahibinden.com/arama?query={val}"

    def __str__(self):
        return f"{self.musteri.ad_soyad} - Sahibinden: {self.sahibinden}"
      
class MusteriFacebook(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='facebooklar')
    facebook = models.CharField(max_length=255, verbose_name="Facebook Kullanıcı Adı veya Linki", blank=True, null=True)

    def get_url(self):
        if not self.facebook:
            return "#"
        val = self.facebook.strip()
        if val.startswith('http://') or val.startswith('https://'):
            return val
        return f"https://facebook.com/{val.lstrip('@')}"
    
class MusteriGoogleMaps(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='haritalar')
    google_maps = models.CharField(max_length=500, verbose_name="Google Maps Konum Linki", blank=True, null=True)

class MusteriIban(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE, related_name='ibanlar')
    iban = models.CharField(max_length=50, verbose_name="IBAN Numarası", blank=True, null=True)