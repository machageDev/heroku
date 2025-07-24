from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Car

def home(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {'cars': cars})

def add_to_cart(request, car_id):
    cart = request.session.get('cart', [])
    if car_id not in cart:
        cart.append(car_id)
    request.session['cart'] = cart
    return redirect('home')
