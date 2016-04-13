from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse

from .models import UserProfile, Installation


def index(request):
    users = get_list_or_404(UserProfile)
    installs = get_list_or_404(Installation)
    # TODO: Add last registered, most active stats?

    return render(request, 'core/home.html', {'installs': len(installs), 'users': len(users)})


def install_detail(request, install_id):
    install = get_object_or_404(Installation, id=install_id)
    return render(request, 'core/rig.html',  {'install': install})


def user_detail(request, user_id):
    user = get_object_or_404(UserProfile, user=user_id)
    installs = get_list_or_404(Installation, owner=user)

    context = {'user': user, 'installs': installs}
    return render(request, 'core/user.html', context)
