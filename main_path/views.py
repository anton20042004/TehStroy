from django.shortcuts import render


def index(request):
    return render(request, 'main_path/index.html')


def projects(request):
    return render(request, 'main_path/projects.html')


def services(request):
    return render(request, 'main_path/services.html')