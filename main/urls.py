from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PazarList, name='pazar-list'),
    url(r'detail/(?P<id>[0-9]+)/$', views.PazarDetail, name='detail'),
    url(r'detail/bolum/(?P<id>[0-9]+)/$', views.BolumDetail, name='detail-bolum'),
    url(r'detail/reyon/(?P<id>[0-9]+)/$', views.ReyonDetail, name='detail-reyon'),
    url(r'detail/uruntipi/(?P<id>[0-9]+)/$', views.UrunTipiDetail, name='detail-uruntipi'),
    url(r'detail/urunadi/(?P<id>[0-9]+)/$', views.UrunAdiDetail, name='detail-urunadi'),
    url(r'detail/urunozellik/(?P<id>[0-9]+)/$', views.UrunOzellikDetail, name='detail-urunozellik'),
    
    url(r'update/(?P<id>[0-9]+)/$', views.PazarUpdate, name='update'),
    url(r'update/bolum/(?P<id>[0-9]+)/$', views.BolumUpdate, name='update-bolum'),
    url(r'update/reyon/(?P<id>[0-9]+)/$', views.ReyonUpdate, name='update-reyon'),
    url(r'update/uruntipi/(?P<id>[0-9]+)/$', views.UrunTipiUpdate, name='update-uruntipi'),
    url(r'update/urunadi/(?P<id>[0-9]+)/$', views.UrunAdiUpdate, name='update-urunadi'),
    url(r'update/urunozellik/(?P<id>[0-9]+)/$', views.UrunOzellikUpdate, name='update-urunozellik'),
   
    url(r'create/$', views.PazarCreate, name='create'),
    url(r'create/bolum/(?P<id>[0-9]+)/$', views.BolumCreate, name='create-bolum'),
    url(r'create/reyon/(?P<id>[0-9]+)/$', views.ReyonCreate, name='create-reyon'),
    url(r'create/uruntipi/(?P<id>[0-9]+)/$', views.UrunTipiCreate, name='create-uruntipi'),
    url(r'create/urunadi/(?P<id>[0-9]+)/$', views.UrunAdiCreate, name='create-urunadi'),
    url(r'create/urunozellik/(?P<id>[0-9]+)/$', views.UrunOzellikCreate, name='create-urunozellik'),
    

    url(r'delete/(?P<id>[0-9]+)/$', views.PazarDelete, name='delete'),
    url(r'delete/bolum/(?P<id>[0-9]+)/$', views.BolumDelete, name='delete-bolum'),
    url(r'delete/reyon/(?P<id>[0-9]+)/$', views.ReyonDelete, name='delete-reyon'),
    url(r'delete/uruntipi/(?P<id>[0-9]+)/$', views.UrunTipiDelete, name='delete-uruntipi'),
    url(r'delete/urunadi/(?P<id>[0-9]+)/$', views.UrunAdiDelete, name='delete-urunadi'),
    url(r'delete/urunozellik/(?P<id>[0-9]+)/$', views.UrunOzellikleriDelete, name='delete-urunozellikleri'),
    


]
 
