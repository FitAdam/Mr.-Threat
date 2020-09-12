from django import forms
from django.core.validators import validate_ipv46_address

from .models import IP

import ipaddress

class IP_Form(forms.ModelForm):
    the_ip = forms.GenericIPAddressField()
    #reported  = forms.BooleanField(required=False)
    class Meta:
        model = IP
        fields = ['the_ip']
        labels = {'the_ip': ''}

    def check_if_ip_is_private(self, new_ip):
        return ipaddress.ip_address(new_ip).is_private

    def clean_the_ip(self, *args, **kwargs):
        #cleaned_data = super(IP_Form, self).clean()
        the_ip = self.cleaned_data.get('the_ip')

        if self.check_if_ip_is_private(the_ip):
            raise forms.ValidationError("You can't do a search on internal/ private IP.")
        else:
            return the_ip

       
    
    



