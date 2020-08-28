from django.shortcuts import render, redirect, get_object_or_404
from .models import IP
from .forms import IP_Form



def index(request):
    """The home page for Mr. Threat."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = IP_Form()
    else:
        # POST data submitted; create a blank form.
        form = IP_Form(data=request.POST)
        if form.is_valid():
            """
            new_ip = form.save(commit=False)
            new_ip.reported = form.cleaned_data['reported']
            print(new_ip.the_ip)
            print(new_ip.reported)
            new_ip.save()
            """
            print(form.is_valid())
            form.save()
            return redirect('web_app:the_results')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'web_app/index.html', context)

def the_results(request):
    """Show the reports from APIs."""
    the_ips =  IP.objects.all()
    context = {'the_ips': the_ips}
    return render(request, 'web_app/the_results.html', context)


