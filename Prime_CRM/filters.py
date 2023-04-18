import django_filters
from django_filters import CharFilter, ChoiceFilter, MultipleChoiceFilter, DateFromToRangeFilter
from rest_framework import filters
from django import forms

from .models import *

class ClientFilter(django_filters.FilterSet):

    doc_num = CharFilter(field_name='contract__doc_num', label="Номер договора", lookup_expr='istartswith')
    Surname = CharFilter(field_name='surname', lookup_expr='iregex', label="Фамилия")
    status = ChoiceFilter(field_name='contract__status', choices=Contract.CHOICES, label="Клиенты со статусом договора")
    phone = CharFilter(field_name='phone', label="Номер телефона", lookup_expr='iregex')
    date = DateFromToRangeFilter(field_name='contract__date', label="дата заключения договора")
    address = CharFilter(field_name='address__address', label="Адрес", lookup_expr='iregex')


    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['surname', 'name', 'patronymic']

class ContractsFilter(django_filters.FilterSet):
    address = CharFilter(field_name='address_id__address', label="Адрес", lookup_expr='iregex')
    Surname = CharFilter(field_name='client_id__surname', lookup_expr='iregex', label="Фамилия")
    doc_num = CharFilter(field_name='doc_num', label="Номер договора", lookup_expr='istartswith')
    date = DateFromToRangeFilter(field_name='date', label="дата заключения договора")
    summ = CharFilter(field_name='summ', label="Сумма")
    status = ChoiceFilter(field_name='status', choices=Contract.CHOICES, label="Статус")

    class Meta:
        model = Contract
        fields = '__all__'
