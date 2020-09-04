from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import IP
from .forms import IP_Form

from .abuseipdb import AbuseIPDB
from .virus_total import check_the_ip_with_vt, check_the_votes_with_vt
from .badips import check_the_ip_with_badips


def index(request):
    """The home page for Mr. Threat."""
   
    return render(request, 'web_app/index.html')

@login_required
def search(request):
    """The search site"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = IP_Form()
    else:
        # POST data submitted; create a blank form.
        form = IP_Form(data=request.POST)
        if form.is_valid():

            new_ip = form.save(commit=False)
            new_ip.reported = form.cleaned_data['reported']
            new_ip.owner = request.user
            searched_ip = new_ip.the_ip
            # Check the IP with APIs.
            checked_ip = AbuseIPDB(new_ip.the_ip,90).check_the_ip_with_abuse()
            print(f"This is from abuse {checked_ip}")
            checked_ip_vt = check_the_ip_with_vt(new_ip.the_ip)
            checked_ip_votes_vt = check_the_votes_with_vt(new_ip.the_ip)
            checked_ip_badips = check_the_ip_with_badips(new_ip.the_ip)
            # Save payloads to database.
            new_ip.abuseibdb_payload = checked_ip
            new_ip.virustotal_payload = checked_ip_vt
            new_ip.virustotal_votes_payload = checked_ip_votes_vt
            new_ip.badips_payload = checked_ip_badips
            print(new_ip.virustotal_payload)

            new_ip.save()
            
            context = {'searched_ip': searched_ip, 'checked_ip': checked_ip, 'checked_ip_vt': checked_ip_vt, 'checked_ip_votes_vt': checked_ip_votes_vt, "checked_ip_badips": checked_ip_badips}
            return render(request,'web_app/the_results.html', context)
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'web_app/search.html', context)

@login_required
def the_results(request):
    """Show the reports from APIs."""
    context = {'searched_ip': searched_ip}
    return render(request,'web_app/the_results.html', context)


@login_required
def searched_ips(request):
    the_ips =  IP.objects.all()
    context = {'the_ips': the_ips}
    return render(request, 'web_app/searched_ips.html', context)


@login_required
def the_searched_ip(request, ip_id):
    """Show a single ip from a history"""
    the_ip = IP.objects.get(id=ip_id)

    searched_ip = the_ip.the_ip

    checked_ip = AbuseIPDB(searched_ip,90).check_the_ip_with_abuse()
    checked_ip_vt = check_the_ip_with_vt(the_ip.the_ip)
    checked_ip_votes_vt = check_the_votes_with_vt(the_ip.the_ip)
    checked_ip_badips = check_the_ip_with_badips(the_ip.the_ip)

    context = {'searched_ip': searched_ip, 'checked_ip': checked_ip, 'checked_ip_vt': checked_ip_vt, 'checked_ip_votes_vt': checked_ip_votes_vt, "checked_ip_badips": checked_ip_badips}
    return render(request,'web_app/the_searched_ip.html', context)