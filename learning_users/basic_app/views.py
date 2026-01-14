from django.shortcuts import render, redirect
from basic_app.forms import UserForm, UserProfileInfoForm
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

def index(request):
    return render(request, 'basic_app/index.html')

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

            return redirect('basic_app:profile_preview', user_id=user.id)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })

def profile_preview(request, user_id):
    user = User.objects.get(id=user_id)
    profile = UserProfileInfo.objects.get(user=user)

    return render(request, 'basic_app/profile_preview.html', {
        'user': user,
        'profile': profile
    })