import django_tables2 as tables

class ClientsTable(tables.Table):
    doc_num = tables.Column(accessor="contract__doc_num__min", verbose_name='Первичный договор')
    full_name = tables.Column(accessor="full_name", verbose_name="ФИО")
    address = tables.Column(accessor="address__address", verbose_name="Адрес")
    phone = tables.Column(accessor="phone", verbose_name="Номер телефона")
    contracts = tables.Column(verbose_name="Все договоры")

    class Meta:
        attrs = {"class": "table table-bordered", "data-add-url": "Url here"}
        template_name = "django_tables2/bootstrap4.html"