import django_tables2 as tables
from django.utils.html import format_html
from .models import Client

class ClientsTable(tables.Table):
    contract__doc_num__min = tables.Column(accessor="contract__doc_num__min", verbose_name='Первичный договор', orderable=False)
    full_name = tables.Column(accessor="full_name", verbose_name="ФИО", orderable=False)
    address = tables.Column(accessor="address__address", verbose_name="Адрес", orderable=False)
    phone = tables.Column(accessor="phone", verbose_name="Номер телефона", orderable=False)
    actions = tables.Column(empty_values=(), verbose_name="Действия", orderable=False, accessor="pk")


    class Meta:
        attrs = {"class": "table table-striped table-bordered table-sm", "data-add-url": "Url here"}
        template_name = "django_tables2/bootstrap4.html"



    def render_actions(self, value, record):
        return format_html("<a class='btn btn-primary btn-sm' href='{}'>Договоры</a> "
                           "<a class='btn btn-secondary btn-sm' href='{}'>Изменить</a>"
                           " <a class='btn btn-danger btn-sm' href='{}'>Удалить</a>"
                           .format("/contracts/" + str(record['pk']), "/edit/" + str(record['pk']), "/delete/" + str(record['pk']))
                           )




class ContractsTable(tables.Table):
    pass