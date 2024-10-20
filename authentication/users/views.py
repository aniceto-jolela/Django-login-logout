from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')  # Use cleaned_data to get validated data
			messages.success(request, f' {user} has been created successfully!')
			return redirect('home')
	else:
		form = UserRegisterForm()
		# This line ensures that an HttpResponse is always returned
	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	return render(request, 'users/profile.html')
