from django.db import models

# Create your models here.

class Client(models.Model):
    surname = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    patronymic = models.CharField(max_length=64)
    phone = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return '{} {}'.format(self.name, self.phone)

class Address(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address

class Contract(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.BooleanField()
    summ = models.FloatField()
    description = models.TextField()
    doc_num = models.CharField(max_length=30)

    def __str__(self):
        return self.doc_num