from django.db import models


# Create your models here.

class EmailModel(models.Model):
    sub = models.TextField(max_length=10000, blank=False)
    mes = models.TextField(max_length=100000, blank=False)

    def __str__(self):
        return '{}{}'.format(self.sub, self.mes)

    class Meta:
        get_latest_by = 'id'


class Users(models.Model):
    from_mail = models.EmailField(max_length=300, blank=False)
    to_mail = models.EmailField(max_length=300, blank=False)

    def __str__(self):
        return '{}{}'.format(self.from_mail, self.to_mail)

    class Meta:
        verbose_name = "users"
        verbose_name_plural = "users"
