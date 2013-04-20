from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect


def index(request):
    return render(request, 'index.html', locals())


def dashboard(request):
    return render(request, 'dashboard.html', locals())
