from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from anapneo.neo.models import UserProfile, Neo, Feedback
from anapneo.neo.forms import NeoForm, UserProfileForm, FeedbackForm
from anapneo.decorators import is_logged_in

from datetime import datetime


def index(request):
    if request.user.is_authenticated():
        me = UserProfile.objects.get(user=request.user)
        return render(request, 'index.html', {'me': me})
    return render(request, 'index.html', )


def dashboard(request):
    if request.user.is_authenticated():
        try:
            me = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            display_name = request.user
            return redirect('/register/')
    neos = Neo.objects.all().extra(
           select={
               'display_name': 'SELECT display_name FROM neo_userprofile WHERE neo_userprofile.id = neo_neo.id'
           },
        )

    paginator = Paginator(neos, 50)
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    # If page request (9999) is out of range, deliver last page of results.
    try:
        neo_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        neo_list = paginator.page(paginator.num_pages)

    return render(request, 'dashboard.html', {'neo_list': neo_list, 'page': page})


@is_logged_in
def register(request):
    try:
        me = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        if request.method == 'POST':
            me = User.objects.get(username=request.user)
            form = UserProfileForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.user = me
                f.email = me.email
                form.save()
                return redirect('/dashboard/')
        else:
            form = UserProfileForm()
    return render(request, 'profile_edit_or_create.html', locals())


def neo_view(request, u_id):
    neo = get_object_or_404(Neo.objects.get(id = u_id))
    feedback = FeedbackForm()
    return render(request, 'neo_view.html',
                  {'neo': neo, 'feedback': feedback})


@is_logged_in
def neo_edit(request, u_id):
    try:
        obj = Neo.objects.get_or_create(id=u_id, user=request.user)
        if request.method == 'POST':
            form = NeoForm(request.POST, instance=obj)
            if form.is_valid():
                f = form.save(commit=False)
                f.user = request.user
                form.save()
                return redirect('/dashboard/')
        else:
            form = NeoForm()
        return render(request, 'neo_edit_or_create.html', {'form': form})

    except Neo.DoesNotExist:
        return redirect('/dashboard/')


@is_logged_in
def neo_create(request):
    if request.method == 'POST':
        form = NeoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            curdate = datetime.now()
            latest_no = Neo.objects.filter(created__year=curdate.strftime("%Y"),
                        created__month=curdate.strftime("%m"),
                        created__day=curdate.strftime("%d")).count()
            new_no = latest_no + 1
            tmpid = "%03d" % ( new_no )
            f.no = str(curdate.strftime("%Y%m%d")) + tmpid
            form.save()
            return redirect('/dashboard/')
    else:
        form = NeoForm()
    return render(request, 'neo_edit_or_create.html', {'form': form})



@is_logged_in
def profile_view(request, slug):
    me = get_object_or_404(UserProfile.objects.filter(display_name=slug))
    return render(request, 'profile_view.html', locals())


@is_logged_in
def profile_edit(request, slug):
    me = UserProfile.objects.get(user=request.user)
    if me.display_name != slug:
        return redirect('/dashboard/')
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=me)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
    else:
        form = UserProfileForm(instance=me)
    return render(request, 'profile_edit_or_create.html', locals())


def about(request):
    if request.user.is_authenticated():
        me = UserProfile.objects.get(user=request.user)
        return render(request, 'about.html', {'me': me})
    return render(request, 'about.html', )


def contact(request):
    if request.user.is_authenticated():
        me = UserProfile.objects.get(user=request.user)
        return render(request, 'contact.html', {'me': me})
    return render(request, 'contact.html', )
