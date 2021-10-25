from django.db import models

# Create your models here.
class Berita(models.Model):
    judul = models.CharField(max_length=30)
    tanggalRilis = models.DateField()
    penulis = models.CharField(max_length=20)
    isiBerita = models.CharField(max_length=200)
