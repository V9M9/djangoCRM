from django.db import models

# Create your models here.ч

class Client(models.Model):
    surname = models.CharField(max_length=64, verbose_name="Фамилия", null=True, default='')
    name = models.CharField(max_length=64, verbose_name="Имя", null=True, default='')
    patronymic = models.CharField(max_length=64, verbose_name="Отчество", null=True, default='')
    phone = models.CharField(max_length=20, null=False, blank=False, verbose_name="Номер телефона")

    def __str__(self):
        return '{} {} {}'.format(self.surname, self.name, self.phone)

class Address(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, verbose_name="Адрес")

    def __str__(self):
        return self.address

class Contract(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name="Адрес")
    date = models.DateField(verbose_name="Дата", null=True)
    summ = models.FloatField(verbose_name="Сумма", null=True)
    CHOICES = (
        ('ДА', 'ДА'),
        ('НЕТ', 'НЕТ'),
    )
    status = models.CharField(verbose_name="статус", max_length=15, choices=CHOICES, null=False)
    description = models.TextField(verbose_name="Примечания")
    doc_num = models.CharField(max_length=30, verbose_name="Номер договора", null=True)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.doc_num, self.date, self.summ, self.description, self.status)