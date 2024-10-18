from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def post(request):
    return render(request, 'blog/post.html')