from django.shortcuts import render

from core.models import FoodItem

# Create your views here.


def home(request):
    items = FoodItem.objects.filter(available=True)
    return render(request, 'home.html', {'items': items})
