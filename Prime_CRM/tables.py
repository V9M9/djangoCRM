import django_tables2 as tables
from django.utils.html import format_html
from .models import Client, Contract


class ClientsTable(tables.Table):
    contract__doc_num__min = tables.Column(accessor="contract__doc_num__min", verbose_name='Первичный договор',
                                           orderable=False)
    full_name = tables.Column(accessor="full_name", verbose_name="ФИО", orderable=False)
    address = tables.Column(accessor="address__address", verbose_name="Адрес", orderable=False)
    phone = tables.Column(accessor="phone", verbose_name="Номер телефона", orderable=False)

    last_contract_date = tables.Column(accessor="contract__date__max", verbose_name='Дата последнего договора',
                                           orderable=False)
    actions = tables.Column(empty_values=(), verbose_name="Действия", orderable=False)


    class Meta:
        attrs = {"class": "table table-striped table-bordered table-sm", "data-add-url": "Url here"}
        template_name = "django_tables2/bootstrap4.html"

    def render_actions(self, value, record):
        return format_html("<a class='btn btn-info btn-sm' href='{}'>Договоры</a> "
                           "<a class='btn btn-outline-info btn-sm' href='{}'>Изменить</a>"
                           " <a class='btn btn-danger btn-sm' href='{}'>Удалить</a>"
                           .format("/contracts/" + str(record['pk']), "/edit/" + str(record['pk']),
                                   "/delete/" + str(record['pk']))
                           )


class ClientContractsTable(tables.Table):
    doc_num = tables.Column(accessor="doc_num", orderable=False)
    date = tables.Column(accessor="date", orderable=False)
    summ = tables.Column(accessor="summ", orderable=False)
    description = tables.Column(accessor="description", orderable=False)
    status = tables.Column(accessor="status", orderable=False)
    actions = tables.Column(empty_values=(), verbose_name="Действия", orderable=False, accessor="pk")

    class Meta:
        attrs = {"class": "table table-striped table-bordered table-sm", "data-add-url": "Url here"}
        template_name = "django_tables2/bootstrap4.html"

    def render_actions(self, value, record):
        return format_html("<a class='btn btn-secondary btn-sm' href='{}'>Изменить</a>"
                           " <a class='btn btn-danger btn-sm' href='{}'>Удалить</a>".format(
            "/edit_contract/" + str(record.pk), "/delete_contract/" + str(record.pk))
                           )


class AllContractsTable(tables.Table):
    addr = tables.Column(empty_values=(), orderable=False, verbose_name="Адрес")
    client = tables.Column(empty_values=(), accessor="full_name", orderable=False, verbose_name="Клиент")
    doc_num = tables.Column(accessor="doc_num", orderable=False)
    date = tables.Column(accessor="date", orderable=True)
    summ = tables.Column(accessor="summ", orderable=False)
    description = tables.Column(accessor="description", orderable=False)
    status = tables.Column(accessor="status", orderable=False)
    actions = tables.Column(empty_values=(), verbose_name="Действия", orderable=False, accessor="pk")

    class Meta:
        attrs = {"class": "table table-striped table-bordered table-sm", "data-add-url": "Url here"}
        template_name = "django_tables2/bootstrap4.html"

    def render_actions(self, value, record):
        return format_html("<a class='btn btn-outline-info btn-sm' href='{}'>Изменить</a>"
                           " <a class='btn btn-outline-danger btn-sm' href='{}'>Удалить</a>".format(
            "/edit_contract/" + str(record['pk']), "/delete_contract/" + str(record['pk']))
                           )

    def render_addr(self, value, record):
        return format_html('<a href="/contracts/{}">{}</a>'.format(str(record['client_id']), str(record['address_id__address'])))