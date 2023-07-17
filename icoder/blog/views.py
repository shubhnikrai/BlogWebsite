from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComment
from django.contrib import messages

# Create your views here.
def blogHome(request):
    allPosts=Post.objects.all()
    context = {'allPosts': allPosts}

    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments=BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.sno not in replyDict.keys():
            replyDict[reply.sno]=[reply]
        else:
            replyDict[reply.sno].append(reply)
    context={'post':post,'comments':comments,'user':request.user}
    return render(request,'blog/blogPost.html',context)
   # return HttpResponse('This is blogpost: ')
def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Post.objects.get(sno=postSno)
        parentSno=request.POST.get("parentSno")
        if parentSno=="":
            comment=BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,"Your comment has been posted successfully")
        else:
            parent=BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment=comment,user=user,post=post)

            comment.save()
            messages.success(request,"Your reply has been posted successfully")

        
    return redirect("/blog/{post.slug}")
