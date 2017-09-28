from django import forms

#Nameadress form to be loaded 
class NameaddressForm(forms.Form):
    name_text = forms.CharField(label='Name', max_length=300)
    email_text = forms.EmailField(label='Email' ,max_length=300)
  