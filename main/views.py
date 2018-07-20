from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render,get_object_or_404,redirect
from .models import Pazar,Bolum,Reyon,UrunAdi,UrunTipi,UrunOzellikleri
from .forms import PazarForm,BolumForm,ReyonForm,UrunTipiForm,UrunAdiForm,UrunOzellikleriForm


def PazarList(request): 
    pazarlar=Pazar.objects.all()
    context={
            'pazarlar':pazarlar,
            }
    return render(request,'main/pazar_list.html',context)

def PazarDetail(request,id):
    pazar=get_object_or_404(Pazar,id=id)
    bolum=Bolum.objects.all().filter(pazar_id=id)
    reyon=Reyon.objects.all().filter(pazar_id=id)
    urunadi=UrunAdi.objects.all().filter(pazar_id=id)
    uruntipi=UrunTipi.objects.all().filter(pazar_id=id)
    urunozellikleri=UrunOzellikleri.objects.all().filter(pazar_id=id)
    context = {
        'pazar':pazar,
        'bolum':bolum, 
        'reyon':reyon,
        'urunadi':urunadi,
        'uruntipi':uruntipi,
        'urunozellikleri':urunozellikleri,
    }
    return render(request,'main/detail.html',context)

def BolumDetail(request,id):
    bolum=get_object_or_404(Bolum,id=id)
    reyon=Reyon.objects.all().filter(pazar_id=id)
    urunadi=UrunAdi.objects.all().filter(pazar_id=id)
    uruntipi=UrunTipi.objects.all().filter(pazar_id=id)
    urunozellikleri=UrunOzellikleri.objects.all().filter(pazar_id=id)
    context = {
        'bolum':bolum, 
        'reyon':reyon,
        'urunadi':urunadi,
        'uruntipi':uruntipi,
        'urunozellikleri':urunozellikleri,
    }
    return render(request,'main/detail-bolum.html',context)

def ReyonDetail(request,id):
    reyon=get_object_or_404(Reyon,id=id)
    urunadi=UrunAdi.objects.all().filter(pazar_id=id)
    uruntipi=UrunTipi.objects.all().filter(pazar_id=id)
    urunozellikleri=UrunOzellikleri.objects.all().filter(pazar_id=id)
    context = {
        'reyon':reyon,
        'urunadi':urunadi,
        'uruntipi':uruntipi,
        'urunozellikleri':urunozellikleri,
    }
    return render(request,'main/detail-reyon.html',context)
def UrunTipiDetail(request,id):
    uruntipi=get_object_or_404(UrunTipi,id=id)
    urunadi=UrunAdi.objects.all().filter(pazar_id=id)
    urunozellikleri=UrunOzellikleri.objects.all().filter(pazar_id=id)
    context = {
        'urunadi':urunadi,
        'uruntipi':uruntipi,
        'urunozellikleri':urunozellikleri,
    }
    return render(request,'main/detail-uruntipi.html',context)
def UrunAdiDetail(request,id):
    urunadi=get_object_or_404(UrunAdi,id=id)
    urunozellikleri=UrunOzellikleri.objects.all().filter(pazar_id=id)
    context = {
        'urunadi':urunadi,
        'urunozellikleri':urunozellikleri,
    }
    return render(request,'main/detail-urunadi.html',context)
def UrunOzellikDetail(request,id):
    urunozellikleri=get_object_or_404(UrunOzellikleri,id=id)
    context = {
        'urunozellikleri':urunozellikleri,
    }
    return render(request,'main/detail-urunozellikleri.html',context)

def PazarCreate(request):
    if request.method == "POST":
        form = PazarForm(request.POST)
        if form.is_valid():
            pazar = form.save(commit=False)
            pazar.save()
            return redirect('pazar-list')
    else:
        form = PazarForm()
    return render(request, 'main/create.html', {'form': form})
def BolumCreate(request,id):
    if request.method == "POST":
        form = BolumForm(request.POST)
        if form.is_valid():
            bolum = form.save(commit=False)
            bolum.pazar_id=id
            bolum.save()
            return redirect('pazar-list')
    else:
        form = BolumForm()
    return render(request, 'main/create.html', {'form': form})
def ReyonCreate(request,id):
    bolum=get_object_or_404(Bolum,id=id)
    if request.method == "POST":
        form = ReyonForm(request.POST)
        if form.is_valid():
            reyon = form.save(commit=False)
            reyon.pazar_id=bolum.pazar_id
            reyon.bolum_id=id
            reyon.save()
            return redirect('pazar-list')
    else:
        form = ReyonForm()
    return render(request, 'main/create.html', {'form': form})
def UrunTipiCreate(request,id):
    reyon=get_object_or_404(Reyon,id=id)
    if request.method == "POST":
        form = UrunTipiForm(request.POST)
        if form.is_valid():
            uruntipi = form.save(commit=False)
            uruntipi.pazar_id=reyon.pazar_id
            uruntipi.reyon_id=id
            uruntipi.save()
            return redirect('pazar-list')
    else:
        form = UrunTipiForm()
    return render(request, 'main/create.html', {'form': form})
def UrunAdiCreate(request,id):
    uruntipi=get_object_or_404(UrunTipi,id=id) 
    if request.method == "POST":
        form = UrunAdiForm(request.POST)
        if form.is_valid():
            urunadi = form.save(commit=False)
            urunadi.pazar_id=uruntipi.pazar_id
            urunadi.urunTipi_id=id
            urunadi.save()
            return redirect('pazar-list')
    else:
        form = UrunAdiForm()
    return render(request, 'main/create.html', {'form': form})
def UrunOzellikCreate(request,id):
    urunadi=get_object_or_404(UrunAdi,id=id)
    
    if request.method == "POST":
        form = UrunOzellikleriForm(request.POST)
        if form.is_valid():
            urunozellik = form.save(commit=False)
            urunozellik.pazar_id=urunadi.pazar_id
            urunozellik.urunadi_id=id
            urunozellik.stok=5
            urunozellik.save()
            return redirect('pazar-list')
    else:
        form = UrunOzellikleriForm()
    return render(request, 'main/create.html', {'form': form})

def PazarUpdate(request,id):
    pazar=get_object_or_404(Pazar,id=id)
    bolum=Bolum.objects.all().filter(pazar_id=id)
    reyon=Reyon.objects.all().filter(pazar_id=id)
    uruntipi=UrunTipi.objects.all().filter(pazar_id=id)
    urunadi=UrunAdi.objects.all().filter(pazar_id=id)
    urunoz=UrunOzellikleri.objects.all().filter(pazar_id=id)
    root_id=id
    form=PazarForm(request.POST or None,instance=pazar)
    if form.is_valid():
        pazar=form.save(commit=False)
        pazar.save()
    
    context = {
        'root_id':root_id,
        'form':form,
        'bolum':bolum,
        'reyon':reyon,
        'uruntipi':uruntipi,
        'urunadi':urunadi,
        'urunoz':urunoz,
        }

    return render(request,'main/update.html',context)
def BolumUpdate(request,id):
    bolum=get_object_or_404(Bolum,id=id)
    reyon=Reyon.objects.all().filter(bolum_id=bolum.id)
    uruntipi=UrunTipi.objects.all().filter(reyon_id=reyon.first().id)
    urunadi=UrunAdi.objects.all().filter(urunTipi_id=uruntipi.first().id)
    urunoz=UrunOzellikleri.objects.all().filter(urunadi_id=urunadi.first().id)

    form=BolumForm(request.POST or None,instance=bolum)

    if form.is_valid():
        bolum=form.save(commit=False)
        bolum.save()
    context = {
        'form':form,
        'reyon':reyon,
        'uruntipi':uruntipi,
        'urunadi':urunadi,
        'urunoz':urunoz,
        }
    return render(request,'main/update-bolum.html',context)
def ReyonUpdate(request,id):
    reyon=get_object_or_404(Reyon,id=id)
    form=ReyonForm(request.POST or None,instance=reyon)
    uruntipi=UrunTipi.objects.all().filter(reyon_id=reyon.id)
    urunadi=UrunAdi.objects.all().filter(urunTipi_id=uruntipi.first().id)
    urunoz=UrunOzellikleri.objects.all().filter(urunadi_id=urunadi.first().id)

    if form.is_valid():
        reyon=form.save(commit=False)
        reyon.save()
    context = {
        'form':form,
        'uruntipi':uruntipi,
        'urunadi':urunadi,
        'urunoz':urunoz,
        }
    return render(request,'main/update-reyon.html',context)
def UrunTipiUpdate(request,id):
    uruntipi=get_object_or_404(UrunTipi,id=id)
    form=UrunTipiForm(request.POST or None,instance=uruntipi)
    urunadi=UrunAdi.objects.all().filter(urunTipi_id=uruntipi.id)
    urunoz=UrunOzellikleri.objects.all().filter(urunadi_id=urunadi.first().id)

    if form.is_valid():
        uruntipi=form.save(commit=False)
        uruntipi.save()
    context = {
        'form':form,
        'urunadi':urunadi,
        'urunoz':urunoz,
        }
    return render(request,'main/update-uruntipi.html',context)
def UrunAdiUpdate(request,id):
    urunadi=get_object_or_404(UrunAdi,id=id)
    form=UrunAdiForm(request.POST or None,instance=urunadi)
    urunoz=UrunOzellikleri.objects.all().filter(urunadi_id=urunadi.id)

    if form.is_valid():
        urunadi=form.save(commit=False)
        urunadi.save()
    context = {
        'form':form,
        'urunoz':urunoz,
        }
    return render(request,'main/update-urunadi.html',context)
def UrunOzellikUpdate(request,id):
    urunoz=get_object_or_404(UrunOzellikleri,id=id)
    form=UrunOzellikleriForm(request.POST or None,instance=urunoz)
    if form.is_valid():
        urunoz=form.save(commit=False)
        urunoz.save()
    context = {
        'form':form,
        }
    return render(request,'main/update-urunozellik.html',context)

def PazarDelete(request,id):
    pazar=get_object_or_404(Pazar,id=id)
    pazar.delete()
    return redirect("pazar-list")
def BolumDelete(request,id):
    bolum=get_object_or_404(Bolum,id=id)
    bolum.delete()
    return redirect("pazar-list")
def ReyonDelete(request,id):
    reyon=get_object_or_404(Reyon,id=id)
    reyon.delete()
    return redirect("pazar-list")
def UrunTipiDelete(request,id):
    uruntipi=get_object_or_404(UrunTipi,id=id)
    uruntipi.delete()
    return redirect("pazar-list")
def UrunAdiDelete(request,id):
    urunadi=get_object_or_404(UrunAdi,id=id)
    urunadi.delete()
    return redirect("pazar-list")
def UrunOzellikleriDelete(request,id):
    urunoz=get_object_or_404(UrunOzellikleri,id=id)
    urunoz.delete()
    return redirect("pazar-list")


