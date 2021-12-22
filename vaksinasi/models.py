from django.db import models


# Create your models here.
class Vaksin(models.Model):
    kode = models.CharField(max_length=3, unique = True) 
    kota = models.CharField(max_length=60)
    provinsi = models.CharField(max_length=60)
    lokasi = models.CharField(max_length=60)
    jenis_vaksin = models.CharField(max_length=60)
    tanggal = models.DateField()
    jam_mulai = models.TimeField()
    jam_berakhir = models.TimeField()
    kuota = models.IntegerField()
    
    def add_pendaftar(self):
        self.kuota -= 1
        self.save()
        
class Pendaftar(models.Model):
    kode = models.CharField(max_length=3)
    NIK = models.CharField(max_length=16, unique = True)
    nama_lengkap = models.CharField(max_length = 60)