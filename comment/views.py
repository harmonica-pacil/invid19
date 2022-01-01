
from datetime import datetime
from django.http import response
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt


from users.models import Profile
from .models import Comment,Forum
from .forms import CommentForm
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.http.response import HttpResponse
from django.core import serializers
# There is no local timezone support, you need to know your timezone
import pytz
utc = pytz.timezone('UTC')
localtz = pytz.timezone('Asia/Jakarta')






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
            add_comment.forum_creator =  Forum.objects.get(pk=id)
            add_comment.forum_creator_username = add_comment.forum_creator.creator.username
            add_comment.id_forum = add_comment.forum_creator.pk
            add_comment.comment_creator_username = add_comment.comment_creator.username
            add_comment.creator_image = add_comment.comment_creator.profile_image            
            
            time_stamp = datetime.utcnow()
            utctime = utc.localize(time_stamp)
            time_stamp_jakarta = localtz.normalize(utctime.astimezone(localtz))
            time_stamp_jakarta =time_stamp_jakarta.strftime("%A, %d %B %Y, %I:%M %p")
            add_comment.created_at = time_stamp_jakarta
            add_comment.save()
            
            return HttpResponseRedirect(request.path_info)
    response['form'] = form
    Comment.forum_creator = Forum.objects.get(pk = id)
    
   
    
   
    response['forum'] = Comment.forum_creator
    print("tes",response)



    return render(request,  "comment_list.html", response)


@csrf_exempt
def json_api(request):
    comments = Comment.objects.all()

    data = serializers.serialize('json', Comment.objects.all())
    return HttpResponse(data, content_type="application/json")


@csrf_exempt
def flutter_add(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        print(request.POST)
        print(Profile.objects.all())
        comment.comment_creator = Profile.objects.get(user = request.POST['user'])
        comment.id_forum = request.POST['id'] 
        comment.comment_creator_username = comment.comment_creator.username
        comment.creator_image = comment.comment_creator.profile_image
        comment.created_at = datetime.now().strftime("%A, %d %B %Y, %I:%M %p")
        # print(comment.message)
        
        comment.save()
        print
        return HttpResponseRedirect('../')

    return HttpResponseNotFound("Page not available")   