from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.db.models import Q

from .models import IP, Plan
from .forms import IP_Form

from .abuseipdb import AbuseIPDB
from .virus_total import VirusTotal
from .badips import BadIPs
from .shodan_api import Shodan_API


def index(request):
    """The home page for Mr. Threat."""
    if request.user.is_authenticated == True:
        current_plan = get_object_or_404(Plan, member=request.user.id)
        num = current_plan.number_of_requests
        text = f"{num} searches to use remain in your account."
        messages.info(request, text)
    return render(request, 'web_app/index.html')


@login_required
def search(request):
    """The search site"""
    current_plan = get_object_or_404(Plan, member=request.user.id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = IP_Form()
    else:
        if current_plan.number_of_requests > 0:
            print(current_plan.number_of_requests)
            # POST data submitted; create a blank form.
            form = IP_Form(data=request.POST)
            if form.is_valid():
                # substract a search from the plan
                current_plan.number_of_requests -= 1
                current_plan.save()
                print(current_plan.number_of_requests)

                new_ip = form.save(commit=False)
                new_ip.owner = request.user
                searched_ip = new_ip.the_ip

                # Check the IP with APIs.
                checked_ip_abuseipdb = AbuseIPDB(
                    searched_ip, 90).check_the_ip_with_abuse()
                checked_ip_vt = VirusTotal(
                    searched_ip).check_the_ip_with_vt()
                checked_ip_votes_vt = VirusTotal(
                    searched_ip).check_the_votes_with_vt()
                checked_ip_badips = BadIPs(
                    searched_ip).check_the_ip_with_badips()
                checked_ip_shodan_general_info = Shodan_API(
                    searched_ip).get_general_info()
                checked_ip_shodan_all_banners = Shodan_API(
                    searched_ip).get_all_banners()

                # Save payloads to database.
                new_ip.abuseibdb_payload = checked_ip_abuseipdb
                new_ip.virustotal_payload = checked_ip_vt
                new_ip.virustotal_votes_payload = checked_ip_votes_vt
                new_ip.badips_payload = checked_ip_badips
                new_ip.shodan_general_info_payload = checked_ip_shodan_general_info
                new_ip.shodan_all_banners_payload = checked_ip_shodan_all_banners

                new_ip.save()

                context = {'searched_ip': searched_ip, 'checked_ip_abuseipdb': checked_ip_abuseipdb,
                           'checked_ip_vt': checked_ip_vt, 'checked_ip_votes_vt': checked_ip_votes_vt,
                           "checked_ip_badips": checked_ip_badips,
                           "checked_ip_shodan_general_info": checked_ip_shodan_general_info,
                           "checked_ip_shodan_all_banners": checked_ip_shodan_all_banners}

                """Show the reports from APIs."""
                return render(request, 'web_app/the_results.html', context)
        else:
            messages.error(request, "You have used all your number of searches, buy a plan or comeback tomorrow :)")

    form = IP_Form()
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'web_app/search.html', context)


@login_required
def searched_ips(request):
    the_ips = IP.objects.filter(owner=request.user).order_by('date_checked')
    context = {'the_ips': the_ips}
    return render(request, 'web_app/searched_ips.html', context)


@login_required
def the_searched_ip(request, ip_id):
    """Show a single ip from a history"""
    the_ip = get_object_or_404(IP, id=ip_id)

    searched_ip = the_ip.the_ip

    checked_ip_abuseipdb = the_ip.abuseibdb_payload
    checked_ip_vt = the_ip.virustotal_payload
    checked_ip_votes_vt = the_ip.virustotal_votes_payload
    checked_ip_badips = the_ip.badips_payload
    checked_ip_shodan_general_info = the_ip.shodan_general_info_payload
    checked_ip_shodan_all_banners = the_ip.shodan_all_banners_payload

    context = {'searched_ip': searched_ip, 'checked_ip_abuseipdb': checked_ip_abuseipdb,
               'checked_ip_vt': checked_ip_vt, 'checked_ip_votes_vt': checked_ip_votes_vt,
               "checked_ip_badips": checked_ip_badips,
               "checked_ip_shodan_general_info": checked_ip_shodan_general_info,
               "checked_ip_shodan_all_banners": checked_ip_shodan_all_banners}

    return render(request, 'web_app/the_searched_ip.html', context)
