from django.shortcuts import render

from StoreApp1.forms import StockCreateForm
from StoreApp1.models import Stock
from .forms import StockCreateForm


# Create your views here.
def home(request):
    title = 'Welcome: This is the Home Page'
    form = "We love you"
    context = {
        "title": title,
        "test": form,
    }
    return render(request, "home.html", context)

def list_items(request):
    title = 'This is the List Items'
    queryset = Stock.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "list_items.html", context)

def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_items.html", context)