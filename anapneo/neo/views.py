from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from anapneo.neo.models import UserProfile, UserProfileForm
from anapneo.decorators import is_logged_in


def index(request):
    return render(request, 'index.html', locals())


@is_logged_in
def dashboard(request):
    try:
        me = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('/register/')
    return render(request, 'dashboard.html', locals())


@is_logged_in
def register(request):
    try:
        me = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        if request.method == 'POST':
            user = User.objects.get(username=request.user)
            form = UserProfileForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.user = user
                f.email = user.email
                form.save()
                return redirect('/dashboard/')
        else:
            form = UserProfileForm()
        return render(request, 'register.html', locals())


def neo_view(request, u_id):
    pass


def neo_edit_or_create(request, u_id):
    pass


def profile_view(request, slug):
    pass


def profile_edit_or_create(request, slug):
    pass


def about(request):
    return render(request, 'about.html', locals())


def contact(request):
    return render(request, 'contact.html', locals())
