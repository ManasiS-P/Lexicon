from django.shortcuts import render, redirect
from basic_app.forms import UserForm, UserProfileInfoForm
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You're logged in")

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

            #return redirect('basic_app:profile_preview', user_id=user.id)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })

# def profile_preview(request, user_id):
#     user = User.objects.get(id=user_id)
#     profile = UserProfileInfo.objects.get(user=user)

#     return render(request, 'basic_app/profile_preview.html', {
#         'user': user,
#         'profile': profile
#     })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
           if user.is_active:
               login(request,user)
               return HttpResponseRedirect(reverse('index'))
           else:
               return HttpResponse("Account not active")
           
        else:
            print('Someone tried to login and failed')
            print("Username:{} and password{}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
        
    else:
        return render(request,'basic_app/login.html')