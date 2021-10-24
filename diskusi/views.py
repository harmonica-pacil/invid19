from django.shortcuts import render
from .models import Forum
from .forms import ForumForm
from django.http.response import HttpResponseRedirect
import datetime

def index(request):
    forums = Forum.objects.all().values()
    response = {'forums' : forums}
    return render(request, 'forum_list.html', response)

def add_forum(request):
    #print("halooo")
    form = ForumForm(request.POST)
    if form.is_valid():
        new_forum = form.save(commit=False)
        new_forum.creator = request.user.id

        print(new_forum.creator)
        print(new_forum.created_at)
        print(new_forum.message)
        print(new_forum.title)
        new_forum.save()
        #for field in form:
      #      print(field.value())

        return HttpResponseRedirect('../')

    context = {'form' : form}
    return render(request, 'forum_form.html', context)


