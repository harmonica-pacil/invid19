from django.db import models


class Artikel(models.Model):
    judulArtikel = models.CharField(max_length=30)
    tglRilis = models.DateField(auto_now=True)
    peninjau = models.CharField(max_length=20)
    isiArtikel = models.TextField()
    thumbnail = models.CharField(max_length=500)