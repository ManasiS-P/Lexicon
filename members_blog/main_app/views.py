from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, UserProfileInfo
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from main_app.forms import UserForm, UserProfileInfoForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'main_app/base.html')

def post_list(request):
    posts = Post.objects.all().order_by('-created')[:2]
    return render(request, 'main_app/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    comments = None
    if request.user.is_authenticated():
        comments = post.comments.all()

    return render(request, 'main_app/post_detail.html', {
        'post': post,
        'comments': comments
    })

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            return redirect('main_app:profile_preview', user_id=user.id)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'main_app/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })


@login_required
def profile(request):
    user = request.user
    profile = UserProfileInfo.objects.get(user=user)
    return render(request, 'main_app/profile_preview.html', {
        'user': user,
        'profile': profile
    })

def profile_preview(request, user_id):
    user = User.objects.get(id=user_id)
    profile = UserProfileInfo.objects.get(user=user)

    return render(request, 'main_app/profile_preview.html', {
        'user': user,
        'profile': profile
    })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
           if user.is_active:
               login(request,user)
               return HttpResponseRedirect(reverse('main_app:post_list'))
           else:
               return HttpResponse("Account not active")
           
        else:
            print('Someone tried to login and failed')
            print("Username:{} and password{}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
        
    else:
        return render(request,'main_app/login.html')
