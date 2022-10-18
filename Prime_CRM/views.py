from django.db.models.functions import Concat
from django.db.models import Value as V
from django.shortcuts import render
from .models import Client, Address, Contract
from .tables import ClientsTable

# Create your views here.

def index(request):
    clients = Client.objects.all()
    clients = Client.objects.annotate(full_name=Concat('surname', V(' '), 'name', V(' '), 'patronymic')).values("address__address" ,'full_name', 'phone')
    table = ClientsTable(clients)
    context = {
        "clients": clients,
        "table": table,

    }
    return render(request, "index.html", context)