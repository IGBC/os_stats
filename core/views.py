from django.shortcuts import get_object_or_404, render, get_list_or_404

from .models import UserProfile, Installation
from .forms import UserProfileForm


def index(request):
    users = get_list_or_404(UserProfile)
    installs = get_list_or_404(Installation)
    if users and installs:
        return render(request, 'core/home.html', {'installs': len(installs), 'users': len(users), 'users_list': users})
    else:
        return render(request, 'core/home.html', {'installs': 0, 'users': 0})


def detail_machine(request, install_id):
    machine = get_object_or_404(Installation, id=install_id)
    return render(request, 'core/rig.html',  {'machine': machine})


def detail_user(request, user_id):
    user = get_object_or_404(UserProfile, user=user_id)
    machines = get_list_or_404(Installation, owner=user)

    context = {'user': user, 'installs': machines}
    return render(request, 'core/user.html', context)


def list_users(request):
    users = get_list_or_404(UserProfile)
    return render(request, 'core/users.html', {'users': users})


def list_machines(request):
    machines = get_list_or_404(Installation)
    return render(request, 'core/rigs.html', {'machines': machines})


def signup_user(request):
    return render(request, 'core/signup.html', {})