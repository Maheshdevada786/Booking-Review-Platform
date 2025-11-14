from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect(reverse_lazy('accounts:login'))  # redirect to namespaced login page after signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


    
@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('accounts:profile'))
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect(reverse_lazy('accounts:signup'))
    return render(request, 'confirm_delete.html')


