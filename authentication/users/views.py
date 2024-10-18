from django.shortcuts import render, redirect
from .forms import UserRegister
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            user = form.data.get('username')
            messages.success(request, f'{user} has been created successful!')
            return redirect('home')
    else:
        form = UserRegister()
        return render(request, 'users/register.html', {'frm': form})
