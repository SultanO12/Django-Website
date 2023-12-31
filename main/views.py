from django.shortcuts import render, redirect
from .models import Catigory, Product
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from authentication.models import Profile
from django.contrib import messages

def main_page(request):
    cats = Catigory.objects.all()
    prodcts = Product.objects.all()
    return render(request, "main/index.html", {"cats":cats, "prodcts":prodcts})

def contact_page(request):
    cats = Catigory.objects.all()
    prodcts = Product.objects.all()
    if request.method == 'POST':
        messages.success(request, "Сообщение успешно отправлено!")
        return redirect('index')
    return render(request, "main/contect.html", {"cats":cats})

def about_page(request):
    cats = Catigory.objects.all()
    prodcts = Product.objects.all()
    return render(request, "main/about.html", {"cats":cats})

def products_page(request, category):
    cats = Catigory.objects.all()
    prodcts = Product.objects.all()
    cat = Product.objects.filter(category=category)
    return render(request, "main/products.html", {"cat":cat, "cats":cats})

def detiles_page(request, slug):
    cats = Catigory.objects.all()
    prodcts = Product.objects.all()
    product_title = Product.objects.filter(slug=slug).last()
    products = Product.objects.filter(slug=slug)
    return render(request, "main/detalis.html", context={"cats":cats, "product_title":product_title, "products":products})

class InfoUser(LoginRequiredMixin, View):
    login_url = '/auth/register/'
    redirect_field_name = 'index'
    def get(self, request):
        cats = Catigory.objects.all()
        prodcts = Product.objects.all()
        profile = Profile.objects.filter(user=request.user).first()
        if profile:
            return render(request, "main/account.html", {"cats":cats, "profile":profile})
        return render(request, "main/account.html", {"cats":cats})
    
