from django.db import models
from django.urls import reverse


# Create your models here.
class Karyawan(models.Model):
    nama = models.CharField(max_length=100)
    nomor_handphone = models.CharField(max_length=20)
    alamat = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nama

    def get_absolute_url(self):
        return reverse('karyawan-detail', kwargs={'pk': self.pk})


class Barang(models.Model):
    kode = models.CharField(max_length=4)
    nama = models.CharField(max_length=100)
    jenis = models.CharField(max_length=100)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

    def get_absolute_url(self):
        return reverse('barang-detail', kwargs={'pk': self.pk})


class Inventaris(models.Model):
    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)

    def __str__(self):
        return self.karyawan.nama

    def get_absolute_url(self):
        return reverse('inventaris-detail', kwargs={'pk': self.pk})
