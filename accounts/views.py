from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


def register(request):
    """
    Handle user registration. If the form is valid, save the user and log them in.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def delete_account(request):
    """
    Confirm and delete the current user's account.
    """
    if request.method == 'POST':
        # Delete the user account
        request.user.delete()
        # Redirect to home or login page after deletion
        return redirect('home')
    return render(request, 'accounts/delete_account_confirm.html')
