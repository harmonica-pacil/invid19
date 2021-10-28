from django.shortcuts import render
from .models import Forum
from .forms import ForumForm
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from users.models import Profile
from django.core import serializers
from django.contrib.auth.decorators import login_required

def index_json(request):
    forums = Forum.objects.all()

    for forum in forums:
        forum.creator_username = forum.creator.username
        forum.creator_image = forum.creator.profile_image
        forum.save()
        print(forum.creator_username)

    for forum in forums:
        print(forum.creator_username)

    response = {'forums' : forums.values()}
    print(response)

    data = serializers.serialize('json', Forum.objects.all())
    return HttpResponse(data, content_type="application/json")

def index(request):
    forums = Forum.objects.all().values()
    
    for i in Forum.objects.all():
        print(i.creator)

    response = {'forums' : forums}
    print(response)
    #print(response.Users.id)
    return render(request, 'forum_list.html', response)

@login_required(login_url="login")
def add_forum(request):
    #print("halooo")
    form = ForumForm(request.POST)
    if form.is_valid():
        new_forum = form.save(commit=False)
        new_forum.creator = Profile.objects.get(user = request.user.id)

        print(new_forum.creator)
        print(new_forum.created_at)
        print(new_forum.message)
        print(new_forum.title)
        new_forum.save()
        return HttpResponseRedirect('../')

    context = {'form' : form}
    return render(request, 'forum_form.html', context)


