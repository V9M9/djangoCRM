from django.db import models

# Create your models here.

class Client(models.Model):
    surname = models.CharField(max_length=64, verbose_name="Фамилия")
    name = models.CharField(max_length=64, verbose_name="Имя")
    patronymic = models.CharField(max_length=64, verbose_name="Отчество")
    phone = models.CharField(max_length=20, null=False, blank=False, verbose_name="Номер телефона")

    def __str__(self):
        return '{} {}'.format(self.name, self.phone)

class Address(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, verbose_name="Адрес")

    def __str__(self):
        return self.address

class Contract(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Дата", null=True)
    status = models.BooleanField()
    summ = models.FloatField(verbose_name="Сумма", null=True)
    description = models.TextField(verbose_name="Примечания")
    doc_num = models.CharField(max_length=30, verbose_name="Номер договора")

    def __str__(self):
        return '{} {} {} {}'.format(self.doc_num, self.date, self.summ, self.description)