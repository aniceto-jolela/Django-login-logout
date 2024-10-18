from django.shortcuts import render
from .forms import UserRegister


def register(request):
    form = UserRegister()
    return render(request, 'users/register.html', {'frm': form})
