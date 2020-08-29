from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import IP
from .forms import IP_Form



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
            print(new_ip.the_ip)
            print(new_ip.reported)
            
            new_ip.save()
           
            return redirect('web_app:the_results')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'web_app/search.html', context)

@login_required
def the_results(request):
    """Show the reports from APIs."""
    the_ips =  IP.objects.all()
    context = {'the_ips': the_ips}
    return render(request, 'web_app/the_results.html', context)


