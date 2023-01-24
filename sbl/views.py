from sbl.models import Products
from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'object_list': Products.objects.all()
    }
    return render(request, 'sbl/home.html', context)


def contacts(request):
    return render(request, 'sbl/contacts.html')

