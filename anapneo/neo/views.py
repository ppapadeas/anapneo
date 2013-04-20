from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect


def index(request):
    return render(request, 'index.html', locals())

def dashboard(request):
    return render(request, 'dashboard.html', locals())

def neo_view(request, u_id):
    pass

def neo_edit_or_create(request, u_id):
    pass

def profile_view(request, slug):
    pass

def profile_edit_or_create(request, slug):
    pass
