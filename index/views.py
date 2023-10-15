from django.shortcuts import render, redirect
from . import forms, models
import requests
from .handlers import bot

from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def home_page(request):
    search_bar = forms.SearchForm()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {'form': search_bar, 'products': products, 'categories': categories}
    return render(request, 'index.html', context)


def team(request):
    search_bar = forms.SearchForm()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {'form': search_bar, 'products': products, 'categories': categories}
    return render(request, 'team.html', context)


def magazine(request):
    search_bar = forms.SearchForm()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {'form': search_bar, 'products': products, 'categories': categories}
    return render(request, 'magazine.html', context)

def contacts(request):
    search_bar = forms.SearchForm()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {'form': search_bar, 'products': products, 'categories': categories}
    return render(request, 'contacts.html', context)

def get_exact_category(request, pk):
    category = models.Category.objects.get(id=pk)
    products = models.Product.objects.filter(product_category=category)
    context = {'products': products}
    return render(request, 'exact_category.html', context)

def get_exact_product(request, pk):
    search_bar = forms.SearchForm()
    product = models.Product.objects.get(id=pk)
    context = {'product': product, 'form': search_bar}
    return render(request, 'exact_product.html', context)

def search_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        try:
            exact_product = models.Product.objects.get(product_name__icontains=get_product)
            return redirect(f'product/{exact_product.id}')
        except:
            return redirect('/')


def add_to_cart(request, pk):
    if request.method == 'POST':
        checker = models.Product.objects.get(id=pk)
        product_amount_one = 1
        models.Cart.objects.create(user_id=request.user.id, user_product=checker,
                                   user_product_count=product_amount_one).save()
        return redirect('/magazine')


def user_cart(request):
    cart = models.Cart.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        main_text = 'Вашими резюме заинтересовались!\n\n'
        for i in cart:
            main_text += f'Соискателя: / {i.user_product} / хотят пригласить на собеседование\n'
        bot.send_message(255380566, main_text)
        cart.delete()
        return redirect('/')
    context = {'cart': cart}
    return render(request, 'user_cart.html', context)

def del_from_cart(request, pk):
    product_to_delete = models.Product.objects.get(id=pk)
    models.Cart.objects.filter(user_id=request.user.id, user_product=product_to_delete).delete()
    return redirect('/cart')

def register(request):
    error = ''
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = forms.RegisterForm(request.POST)
    context = {'form': form}
    return render(request, 'registration/register.html', context)


