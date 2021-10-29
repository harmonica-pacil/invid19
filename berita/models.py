from django.db import models

# Create your models here.
class Berita(models.Model):
    judulBerita = models.CharField(max_length=30)
    tanggalRilis = models.DateField(auto_now=True)
    penulis = models.CharField(max_length=20)
    spoiler = models.CharField(max_length=20)
    isiBerita = models.TextField(max_length=200)
