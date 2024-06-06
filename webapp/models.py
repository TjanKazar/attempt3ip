from django.db import models
from django.contrib.auth.models import User

class Prijavnica(models.Model):
    ime = models.CharField(max_length=100, null=True)
    priimek = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    dejavnost = models.CharField(max_length=100, default=None, null=True)
    datumrojstva = models.CharField(max_length=100, default=None, null=True)
    valid = models.BooleanField(null=True, default=None)
    komentar = models.CharField(max_length=255, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 


    def __str__(self):
        return f"{self.ime} {self.priimek}" 