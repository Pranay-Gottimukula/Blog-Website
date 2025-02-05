from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Method for signing up
def sign_up(request):
    if request.method == 'POST':    # Checking if we got POST request
        form = SignUpForm(request.POST)     # Sign up form with request
        if form.is_valid():     # Checking is the form is valid
            form.save()
            return redirect('users-login')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'users/sign_up.html', context)   # Renders Sign Up Page


@login_required     # This method cannot be accessed without logging in
def profile(request):
    if request.method == 'POST':    # Checking if we got POST request

        # Passing instances to pre-fill the forms
        # Forms will be accepted even without changes
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)

        if p_form.is_valid and u_form.is_valid:     # Checking if the both the forms are valid
            u_form.save()
            p_form.save()
            return redirect('users-profile')    # Redirecting to Profile page
    else:

        # Passing instances to pre-fill the form
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)

    context = {
        'p_form': p_form,
        'u_form': u_form,
    }
    return render(request, 'users/profile.html', context)   # Renders the Profile Page
