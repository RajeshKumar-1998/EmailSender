from django.db import models


# Create your models here.

class Email_Model(models.Model):
    sub = models.CharField(max_length=10000000,blank=False)
    mes = models.CharField(max_length=10000000000000000,blank=False)

    def __str__(self):
        return self.sub + self.mes

    class Meta:
        get_latest_by = 'id'

class users(models.Model):
    from_mail = models.EmailField(max_length=300,blank=False)
    to_mail = models.EmailField(max_length=300,blank=False)

    def __str__(self):
        return '{}{}'.format(self.from_mail,self.to_mail)
    class Meta:
        verbose_name = "users"
        verbose_name_plural = "users"