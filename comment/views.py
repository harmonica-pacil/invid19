
from datetime import datetime
from django.http import response
from django.shortcuts import render,redirect

from users.models import Profile
from .models import Comment,Forum
from .forms import CommentForm
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from django.core import serializers





# Create your views here.
def index(request, id):
    forums = Forum.objects.all().values()
    form = CommentForm(request.POST or None )

    
    response={}

    if request.method == "POST":
        if (form.is_valid):
            print(form.is_valid)
            print(form.is_valid())
            add_comment = form.save(commit=False)
            add_comment.forum = Forum.objects.get(pk=id)

            add_comment.comment_creator =  Profile.objects.get(user = request.user.id)
            add_comment.comment_creator_username = add_comment.comment_creator.username
            add_comment.creator_image = add_comment.comment_creator.profile_image            
            add_comment.created_at = datetime.now().strftime("%A, %d %B %Y, %I:%M %p")
            add_comment.save()
            
            # return HttpResponseRedirect('comment:index',request)
            return HttpResponseRedirect(request.path_info)
    response['form'] = form
    Comment.forum_creator = Forum.objects.get(pk = id)
    
    tes = Comment.forum_creator = Forum.objects.get(pk = id)
    print("TES FORUM:",tes.id)
    Comment.comment_creator = Profile.objects.get(user = request.user.id)            
    print("TES", Comment.forum_creator,  "comment:",Comment.comment_creator)
    response['forum'] = Comment.forum_creator



    return render(request,  "comment_list.html", response)

# def json_api(request):

#     data = serializers.serialize('json', Comment.objects.all())
#     return HttpResponse(data, content_type="application/json")




def json_api(request):
    comments = Comment.objects.all()
    for i in comments:
        print(i.forum_creator.id)
        print(i.comment_creator)

   
        
        
        # comment.save()
        # print(comment.comment_creator)

    for comment in comments:
        print(comment.comment_creator_username)

    response = {'comments' : comments.values()}
    print(response)

    data = serializers.serialize('json', Comment.objects.all())
    return HttpResponse(data, content_type="application/json")
