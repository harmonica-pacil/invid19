from django.db import models

# Create your models here.
class Artikel(models.Model):
    judulArtikel = models.CharField(max_length=30)
    tanggalRilis = models.DateField()
    peninjau = models.CharField(max_length=20)
    isiArtikel = models.CharField(max_length=200)

