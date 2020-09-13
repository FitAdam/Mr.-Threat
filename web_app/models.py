from django.db import models
from django.contrib.auth.models import User

class IP(models.Model):
    """The IP checked by the user."""
    the_ip = models.GenericIPAddressField(default='192.168.0.1')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    reported = models.BooleanField(default=False)
    date_checked = models.DateTimeField(auto_now_add=True)
    abuseibdb_payload = models.JSONField(default=dict)
    virustotal_payload = models.JSONField(default=dict)
    virustotal_votes_payload = models.JSONField(default=dict)
    badips_payload = models.JSONField(default=dict)
    shodan_general_info_payload = models.TextField(default='No data available')
    shodan_all_banners_payload = models.TextField(default='No data available')

    def __str__(self):
        """Return a string representation of the model."""
        return self.the_ip
    
        

class Plan(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.CharField(default='Basic', max_length=100)
    number_of_requests = models.IntegerField(default=5)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.plan