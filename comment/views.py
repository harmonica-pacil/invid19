from django.http import response
from django.shortcuts import render,redirect

from users.models import Profile
from .models import Comment,Forum
from .forms import CommentForm
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from django.core import serializers





# Create your views here.
def index(request):
    forums = Forum.objects.all().values()
    form = CommentForm(request.POST or None )

    # for i in Comment.objects.all():
    #     print(i)
    
    response = {'forums' : forums}

    if request.method == "POST":
        if (form.is_valid):
            add_comment = form.save(commit=False)
            add_comment.forum = Profile.objects.get(creator = request.user.id)

            return redirect('comment:index')
    response['form'] = form
    Comment.creator = Profile.objects.get(user = request.user.id)            
    # print(response)
    return render(request,  "comment_list.html", response)

# def json_api(request):

#     data = serializers.serialize('json', Comment.objects.all())
#     return HttpResponse(data, content_type="application/json")




def json_api(request):
    comments = Comment.objects.all()

    for comment in comments:
        comment.creator_username = comment.creator.username
        comment.creator_image = comment.creator.profile_image
        comment.save()
        print(comment.creator_username)

    for comment in comments:
        print(comment.creator_username)

    response = {'comments' : comments.values()}
    print(response)

    data = serializers.serialize('json', Comment.objects.all())
    return HttpResponse(data, content_type="application/json")
