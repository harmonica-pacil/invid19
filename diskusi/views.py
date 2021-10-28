from django.shortcuts import render
from .models import Forum
from .forms import ForumForm
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from users.models import Profile
from django.core import serializers
from django.contrib.auth.decorators import login_required
from datetime import datetime

def index_json(request):
    forums = Forum.objects.all()

    for forum in forums:
        forum.creator_username = forum.creator.username
        forum.creator_image = forum.creator.profile_image
        forum.save()

    response = {'forums' : forums.values()}

    data = serializers.serialize('json', Forum.objects.all())
    return HttpResponse(data, content_type="application/json")

def index(request):
    response = {}
    return render(request, 'forum_list.html', response)

@login_required(login_url="login")
def add_forum(request):
    form = ForumForm(request.POST)
    if form.is_valid():
        new_forum = form.save(commit=False)
        new_forum.creator = Profile.objects.get(user = request.user.id)
        new_forum.creator_username = new_forum.creator.username
        new_forum.creator_image = new_forum.creator.profile_image
        new_forum.created_at = datetime.now()

        new_forum.save()
        return HttpResponseRedirect('../')

    context = {'form' : form}
    return render(request, 'forum_form.html', context)


