from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for Mr. Threat."""
    return render(request, 'web_app/index.html')