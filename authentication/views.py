from django.shortcuts import render, redirect
from .forms import UserCreateForm
from django.contrib import messages


def signup(request):
    if request.POST:
        print('inside post')
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserCreateForm()
    context = {
        'form': form
    }
    return render(request, 'authentication/signup.html', context=context)
