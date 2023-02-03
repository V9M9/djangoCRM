from django.db.models.functions import Concat
from django.db.models import Value as V, Min
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .models import Client, Address, Contract
from .tables import ClientsTable, ContractsTable
from .forms import ClientForm, AddressForm, MultiForm, ContractForm


# Create your views here.

def index(request):
    clients = Client.objects.annotate(full_name=Concat('surname', V(' '), 'name', V(' '), 'patronymic')) \
        .values("address__address", 'full_name', 'phone', 'pk') \
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
    client_name = Client.objects.values_list('name', flat=True).filter(id=pk)[0]
    client_surname = Client.objects.values_list('surname', flat=True).filter(id=pk)[0]
    client_patronymic = Client.objects.values_list('patronymic', flat=True).filter(id=pk)[0]

    table = ContractsTable(contracts)
    table.paginate(page=request.GET.get("page", 1), per_page=6)

    context = {
        "client_surname": client_surname,
        "client_name": client_name,
        "client_patronymic": client_patronymic,
        "pk": pk,
        "contracts": contracts,
        "table": table,
    }

    return render(request, "contracts.html", context)


class ContractAddView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = "add_contract.html"

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()

        initial['client_id'] = Client.objects.get(pk=self.kwargs['pk'])
        initial['address_id'] = Address.objects.get(client_id=self.kwargs['pk'])
        return initial

    def get_success_url(self):
        print(self.object.client_id.pk)
        return reverse_lazy('show-contracts', kwargs={'pk': self.kwargs['pk']})


class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = "contract_update_form.html"

    def get_success_url(self):
        return reverse_lazy('show-contracts', kwargs={'pk': self.object.client_id.pk})
