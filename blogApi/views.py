from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from .models import Post, Likes, Profile, Comments
from .forms import PostForm ,PostFormSecond, CategoryForm, ProfileForm, AddCommentForm
from django.shortcuts import get_object_or_404
from django.http import Http404


def addChildComment(request, pk):
    parentComment = get_object_or_404(Comments, id=pk)
    postObj = parentComment.article
    if request.method == 'POST':
        formObj = AddCommentForm(request.POST)
        if formObj.is_valid():
            newInstance = Comments.objects.create(commentator=request.user, article=postObj,
                                                  comment=formObj.cleaned_data["comment"], parent=parentComment)
            newInstance.save()
            return redirect('/home/{}'.format(postObj.id))
        else:
            context = {}
            context['form'] = formObj
            return render(request, 'add_comment.html', context)
    else:
        formObj = AddCommentForm()
        context = {}
        context['form'] = formObj
        return render(request, 'add_comment.html', context)

def deleteCommentView(request, pk):
    try:
        commentObj = Comments.objects.get(id=pk)
    except Comments.DoesNotExist:
        raise Http404("This profile does not exist")
    post_id = commentObj.article.id
    if request.user.is_authenticated and request.user.id==commentObj.commentator.id:
        commentObj.delete()
        return redirect('/home/{}'.format(post_id))
    else:
        return HttpResponse(request, "You can not Delete this post !!!!!!!!!!")

def addParentCommentView(request, pk):
    postObj = get_object_or_404(Post,id=pk)
    if request.method == 'POST':
        formObj = AddCommentForm(request.POST)
        if formObj.is_valid():
            newInstance = Comments.objects.create(commentator=request.user, article=postObj,comment=formObj.cleaned_data["comment"])
            newInstance.save()
            return redirect('/home/{}'.format(pk))
        else:
            context = {}
            context['form'] = formObj
            return render(request, 'add_comment.html', context)
    else:
        formObj = AddCommentForm()
        context = {}
        context['form'] = formObj
        return render(request, 'add_comment.html', context)




def createAuthorProfileView(request):
    if request.user.is_authenticated:
        try:
            getObj = request.user.profile
            response = HttpResponse("You already have an existing account")
            return response
        except:
            if request.method=='POST':
                formObj = ProfileForm(request.POST, request.FILES)
                if formObj.is_valid():
                    newInstance = Profile.objects.create(user=request.user, bio=formObj.cleaned_data["bio"],
                                                      portfolio_url=formObj.cleaned_data["portfolio_url"],
                                                      linkedin_url=formObj.cleaned_data["linkedin_url"],
                                                      profile_pic=formObj.cleaned_data["profile_pic"])
                    newInstance.save()
                    return redirect('/home/')
                else:
                    context = {}
                    context['form_obj'] = formObj
                    return render(request, 'create_author_profile.html', context)
            else:
                formObj = ProfileForm()
                context = {}
                context['form_obj'] = formObj
                return render(request, 'create_author_profile.html', context)
    else:
        response = HttpResponse("You are not logged in")
        return response




def editAuthorProfileView(request, pk):
    if request.user.is_authenticated:
        try:
            profileObject = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404("This profile does not exist")

        if request.method=='POST':
            formObj = ProfileForm(request.POST, request.FILES, instance=profileObject)
            if formObj.is_valid():
                formObj.save()
                return redirect('/home/')
            else:
                context = {}
                context['form_obj'] = formObj
                return render(request, 'edit_author_profile.html', context)
        else:
            formObj = ProfileForm(instance=profileObject)
            context = {}
            context['form_obj'] = formObj
            context['userId'] = profileObject.user.id
            return render(request, 'edit_author_profile.html', context)
    else:
        response = HttpResponse("You are not logged in")
        return response


def authorProfileView(request, pk):
    profileObj = get_object_or_404(Profile, id=pk)
    context = {}
    context['profile_obj'] = profileObj
    return render(request, 'author_profile.html', context)


def likeDislikeView(request, pk):
    if request.user.is_authenticated:
        userAuther = request.user
        postObject = Post.objects.get(pk=pk)
        if Likes.objects.filter(auther=userAuther, article=postObject).exists()==False:
            likeObject = Likes(auther=userAuther, article=postObject)
            likeObject.save()
        else:
            obj = Likes.objects.filter(auther=userAuther, article=postObject)
            obj.delete()
        return redirect('/home/'+str(pk))
    else:
        response = HttpResponse("Hey you can not like or Dislike without logging in")
        return response


def createPostView(request):
    if request.method == 'POST':
        new_form = PostForm(request.POST, request.FILES)
        if new_form.is_valid():
            #print(new_form.cleaned_data)
            newInstance = Post.objects.create(auther = request.user, title = new_form.cleaned_data["title"],
                        title_tag = new_form.cleaned_data["title_tag"], body = new_form.cleaned_data["body"], header_image=new_form.cleaned_data["header_image"])
            #instance = new_form.save()
            newInstance.save()
            return redirect('/home/'+str(newInstance.id))
    else:
        new_form = PostForm()
    context = {'form': new_form}
    return render(request, 'add_post.html', context)

class CategoryView:
    def createCategoryView(request):
        if request.method == 'POST':
            new_form = CategoryForm(request.POST)
            if new_form.is_valid():
                instance = new_form.save()
                return redirect('/home/')
        else:
            new_form = CategoryForm()
        context = {'form': new_form}
        return render(request, 'Add_Category.html', context)

    def allCategoryView(request, pk):
        querySet = Post.objects.filter(category=pk.replace('-', ' '))
        return render(request, 'get_all_category_post.html', {'post_object': querySet, 'category': pk.replace('-', ' ') })


def updatePostView(request, pk):
    instance = Post.objects.get(pk=pk)
    if request.method=='POST':
        form = PostFormSecond(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance = form.save()
            return redirect('/home/' + str(instance.id))
    else:
        form = PostFormSecond(instance=instance)
    userId = instance.auther.id
    context = {'form': form, 'userId': userId }
    return render(request, 'update_article.html', context)


def delPostView(request, pk):
    instance = Post.objects.get(pk=pk)
    if request.method=='POST':
        instance.delete()
        return redirect('/home/')
    userId = instance.auther.id
    return render(request, 'delete-post.html', {'post': instance, 'userId': userId})


class PostView(View):
    def get(self, request):
        post_objects = Post.objects.order_by('-date_publication')
        return render(request, 'home.html', {'post_object': post_objects})


class DetailArticleView(View):
    def get(self, request, pk):
        postObject = Post.objects.get(id=pk)
        if request.user.is_authenticated:
            context = self.getContext(request.user, postObject)
        else:
            context = {}
        context['post'] = postObject
        context['all_parent_comments'] = Comments.nonParent.filter(article=postObject)
        context['likeCount'] = self.getLikeCount(postObject)
        return render(request, 'article_detail.html', context)

    def getContext(self, userAuther, postObject):
        context = {}
        context['Liked'] = False
        if Likes.objects.filter(auther=userAuther, article=postObject).exists():
            context['Liked'] = True
        return context

    def getLikeCount(self, postObject):
        return Likes.objects.filter(article= postObject).count()









