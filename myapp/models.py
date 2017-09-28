
import datetime

from django.db import models
from django.forms import ModelForm
from django.utils import timezone



# Create your models here.
#database Nameaddress to store Names and emails
class Nameaddress(models.Model):
    name_text    = models.CharField(max_length=250)
    email_text   = models.EmailField(max_length=250, unique=True)
    status_bool  = models.BooleanField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.name_text

class NameaddressForm(ModelForm):
    class Meta:
        model = Nameaddress
        fields = ['name_text', 'email_text']

