from django.forms import ModelForm, inlineformset_factory

from .models import Pazar, Bolum,Reyon,UrunAdi,UrunTipi,UrunOzellikleri


class PazarForm(ModelForm):
    class Meta:
        model = Pazar
        fields=['isim','yonetim','adres']
        exclude = ()


class BolumForm(ModelForm):
    class Meta:
        model = Bolum
        fields=['bolum_isim','pozisyon']
        exclude = ()

class ReyonForm(ModelForm):
    class Meta:
        model = Reyon
        fields=['numara','saticiAdi']
        exclude = ()

class UrunTipiForm(ModelForm):
    class Meta:
        model = UrunTipi
        fields=['tip_ismi']
        exclude = ()

class UrunAdiForm(ModelForm):
    class Meta:
        model = UrunAdi
        fields=['urun_isim']
        exclude = ()
                                           
class UrunOzellikleriForm(ModelForm):
    class Meta:
        model = UrunOzellikleri
        fields=['ozellikAdi','urunFiyati']
        exclude = ()
                    