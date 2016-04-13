from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse

from .models import UserProfile, Installation

def index(request):
    """
    Dummy function to return some shit
    """
    return HttpResponse('Hello World! Welcome to OS Stats v0.1')


def install_detail(request, install_id):
    return HttpResponse("You're looking at question")


def user_detail(request, user_id):
    user = get_object_or_404(UserProfile, user=user_id)
    installs = get_list_or_404(Installation, owner=user)

    context = {'user': user, 'installs': installs}
    return render(request, 'core/user.html', context)
