from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# app imports
from .forms import CreateUserForm, AccountUpdateForm
from web_app.models import Plan



def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = CreateUserForm()
    else:
        # Process completed form.
        form = CreateUserForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Welcome at our service ' + user)
            # Log the user in and then redirect to home page.
            login(request, new_user)
            new_plan = Plan(member=new_user, plan='Basic',number_of_requests=3)
            new_plan.save()
            return redirect('web_app:search')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required
def account_view(request):
    """ Update account details """

    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {}
    
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        
        form = AccountUpdateForm(

            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

        
        
    current_plan = get_object_or_404(Plan, member=request.user.id)
    num = current_plan.number_of_requests
    text = f"{num} searches to use remain in your account."
    messages.info(request, text)
    context['plan'] = current_plan
    context['account_form'] = form
    

    return render(request, "registration/account.html", context)

