from __future__ import unicode_literals
from django.db import models
from django.urls import reverse

class Pazar(models.Model):
    isim = models.CharField(max_length=100)
    yonetim = models.CharField(max_length=100)
    adres = models.CharField(max_length=100)
    def get_absolute_url(self):
        
        return reverse('update', kwargs={'pk': self.pk})

    def __str__(self):
        return self.isim


class Bolum(models.Model):
    pazar = models.ForeignKey('Pazar',
                              on_delete=models.CASCADE,
                              )
    bolum_isim = models.CharField(max_length=100)
    pozisyon = models.CharField(max_length=100)
    def __str__(self):
        return self.bolum_isim
    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})


class Reyon(models.Model):
 	bolum=models.ForeignKey(
 	Bolum,
 	on_delete=models.CASCADE,
 	)
 	pazar = models.ForeignKey('Pazar',default=1)
 	numara=models.CharField(max_length=100)
 	saticiAdi=models.CharField(max_length=100)
 	def get_absolute_url(self):
 	 	return reverse('update', kwargs={'pk': self.pk})

 	def __str__(self):
 	    return self.numara
    


class UrunTipi(models.Model):
 	reyon=models.ForeignKey(Reyon,
 	on_delete=models.CASCADE,
 	)
 	pazar = models.ForeignKey('Pazar',default=1)
 	tip_ismi=models.CharField(max_length=30)
 	def get_absolute_url(self):
 	    return reverse('update', kwargs={'pk': self.pk})

 	def __str__(self):
 	    return self.tip_ismi
  

class UrunAdi(models.Model):
 	urunTipi=models.ForeignKey(UrunTipi,
 	on_delete=models.CASCADE,
 	)
 	urun_isim=models.CharField(max_length=30)
 	pazar = models.ForeignKey('Pazar',default=1)
 	def get_absolute_url(self):
 	    return reverse('update', kwargs={'pk': self.pk})

 	def __str__(self):
 	    return self.urun_isim
    
class UrunOzellikleri(models.Model):
 	urunadi=models.ForeignKey(UrunAdi,on_delete=models.CASCADE)
 	ozellikAdi=models.CharField(max_length=10)
 	urunFiyati=models.CharField(max_length=10)
 	pazar = models.ForeignKey('Pazar',default=1)
 	stok=models.PositiveIntegerField()
 	def get_absolute_url(self):
 	 	return reverse('update', kwargs={'pk': self.pk})

 	def __str__(self):
 	    return self.ozellikAdi
 	