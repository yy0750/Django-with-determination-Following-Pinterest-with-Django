from symbol import decorated

from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def decorator_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated