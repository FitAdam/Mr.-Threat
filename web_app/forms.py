from django import forms

from .models import IP


class IP_Form(forms.ModelForm):
    the_ip = forms.GenericIPAddressField()
    reported  = forms.BooleanField(required=False)
    class Meta:
        model = IP
        fields = ['the_ip']
        labels = {'the_ip': ''}

"""
class IP_Form_Report(forms.ModelForm):
    reported  = forms.BooleanField(required=False)
    class Meta:
        model = IP
   """     