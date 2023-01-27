from django.db.models.functions import Concat
from django.db.models import Value as V, Min
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .models import Client, Address, Contract
from .tables import ClientsTable
from .forms import ClientForm, AddressForm, MultiForm


# Create your views here.

def index(request):
    clients = Client.objects.annotate(full_name=Concat('surname', V(' '), 'name', V(' '), 'patronymic'))\
        .values("address__address", 'full_name', 'phone', 'pk')\
        .annotate(Min('contract__doc_num'))
    sort = request.GET.get('sort', None)
    if sort:
        clients = clients.order_by(sort)
    table = ClientsTable(clients)
    table.paginate(page=request.GET.get("page", 1), per_page=6)
    context = {
        "clients": clients,
        "table": table,

    }

    return render(request, "index.html", context)

class ClientAddView(CreateView):
    form_class = MultiForm
    success_url = reverse_lazy('index')
    template_name = "add_update.html"

    def form_valid(self, form):
        client = form['client'].save()
        address = form['address'].save(commit=False)
        # contract = form['contract'].save(commit=False)

        address.client_id = client
        address.save()

        # contract.client_id = client
        # contract.address_id = address
        # contract.save()
        return redirect('index')



class ClientUpdateView(UpdateView):

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('index')
    template_name = "client_update_form.html"



class ClientUpdateView(UpdateView):

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('index')
    template_name = "client_update_form.html"


class ClientDeleteView(DeleteView):

    model = Client
    template_name = "client_confirm_delete.html"
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(ClientDeleteView, self).post(request, *args, **kwargs)


def ContractView(request, pk):
    contracts = Contract.objects.all().filter(client_id=pk)

    context = {
        "contracts": contracts,
    }

    return render(request, "contracts.html", context)