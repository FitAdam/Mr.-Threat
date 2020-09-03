from django.db import models
from django.contrib.auth.models import User

class IP(models.Model):
    """The IP checked by the user."""
    the_ip = models.GenericIPAddressField(default='192.168.0.1')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    reported = models.BooleanField(default=False)
    date_checked = models.DateTimeField(auto_now_add=True)
    abuseibdb_payload = models.TextField(default='No data available')
    virustotal_payload = models.TextField(default='No data available')
    badips_payload = models.TextField(default='No data available')

    def __str__(self):
        """Return a string representation of the model."""
        return self.the_ip
    
        