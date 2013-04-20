# -*- coding: utf-8 *-*
from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect


def is_logged_in(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated():
            return function(request, *args, **kwargs)
        else:
            messages.error(request, 'Permission denied.')
            return redirect('/')

    return wrap
