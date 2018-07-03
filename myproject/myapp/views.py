from django.shortcuts import render,render_to_response
from .models import Company


# Create your views here.


def index(request):  # Define our function, accept a request

    items = Company.objects.all()  # ORM queries the database for all of the to-do entries.

    return render_to_response('index.html', {'items': items})
