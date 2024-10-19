from django.shortcuts import render
from django.contrib.auth.decorators import login_required


day_dev = [{'author': 'Dev', 'post':'A day program is a community-based program that provides services to adults with developmental disabilities or other conditions. Day programs can help people develop skills to live in their community, such as: Self-help and self-care, Social and recreational skills, Self-advocacy and employment skills, Community integration skills, and Behavior management. '}]


def home(request):
    return render(request, 'blog/home.html')


@login_required
def about(request):
    return render(request, 'blog/about.html')


@login_required
def post(request):
    dev = {'day_dev': day_dev}
    return render(request, 'blog/post.html', dev)
