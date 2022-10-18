import django_tables2 as tables
from .models import Client, Address, Contract
from django.db.models.functions import Concat
from django.db.models import Value as V


class ClientsTable(tables.Table):
    doc_num = tables.Column(accessor="contract__doc_num", verbose_name='Первичный договор')
    full_name = tables.Column(accessor="full_name", verbose_name="ФИО")
    address = tables.Column(accessor="address__address", verbose_name="Адрес")
    phone = tables.Column(accessor="phone", verbose_name="Номер телефона")
    contracts = tables.Column(verbose_name="Все договоры")

    class Meta:
        pass