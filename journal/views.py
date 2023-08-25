
from django.shortcuts import render, redirect


from .forms import CreateUserForm, LoginForm, PostThoughtForm, UpdateThoughtForm, UpdateUserForm, UpdateProfileForm

from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


from django.contrib import messages

from .models import Thought, Profile


from django.core.mail import send_mail

from django.conf import settings


# Homepage
def home(request):

    return render(request, 'index.html')


# Register
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            current_user = form.save(commit=False)

            form.save()

            send_mail("Welcome to Edenthought " + current_user.username + "!", "Congratulations on creating your account!",
                      settings.DEFAULT_FROM_EMAIL, [ current_user.email ])

            # Create a blank object for a single instance with a foreign key attached
            profile = Profile.objects.create(user=current_user)

            messages.success(request, "Account created")

            return redirect('my-login')
    
    context = {'form':form}

    return render(request, 'register.html', context)


# Login
def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user:

                auth.login(request, user)

                messages.success(request, "Login success")

                return redirect('dashboard')
            
    context = {'form':form}

    return render(request, 'my-login.html', context)


# Dashboard
@login_required(login_url='my-login')
def dashboard(request):

    profile_pic = Profile.objects.get(user=request.user)

    context = {'profilePic':profile_pic}

    return render(request, 'profile/dashboard.html', context)


# User Logout
def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success")

    return redirect('my-login')


# Post Thought
@login_required(login_url='my-login')
def post_thought(request):
    
    form = PostThoughtForm()

    if request.method == "POST":

        form = PostThoughtForm(request.POST)

        if form.is_valid():

            thought = form.save(commit=False)

            thought.user = request.user

            thought.save()

            messages.success(request, "Thought posted")

            return redirect('my-thoughts')
    
    context = {'form':form}

    return render(request, 'profile/post-thought.html', context)


# Update thought
@login_required(login_url='my-login')
def update_thought(request, pk):

    thought = Thought.objects.get(id=pk)

    form = UpdateThoughtForm(instance=thought)

    if request.method == "POST":

        form = UpdateThoughtForm(request.POST, instance=thought)

        if form.is_valid():

            form.save()

            messages.success(request, "Thought updated")

            return redirect('my-thoughts')

    context = {'form':form}

    return render(request, 'profile/update-thought.html', context)


# Delete thought
@login_required(login_url='my-login')
def delete_thought(request, pk):

    thought = Thought.objects.get(id=pk)

    if request.method == "POST":

        thought.delete()

        messages.success(request, "Thought deleted")

        return redirect('my-thoughts')
    
    return render(request, 'profile/delete-thought.html')



# My thoughts
@login_required(login_url='my-login')
def my_thoughts(request):

    current_user = request.user

    thoughts = Thought.objects.all().filter(user=current_user)

    context = {'thoughts': thoughts}

    return render(request, 'profile/my-thoughts.html', context)


# Profile management
@login_required(login_url='my-login')
def profile_management(request):

    form = UpdateUserForm(instance=request.user)

    profile = Profile.objects.get(user=request.user)

    form_2 = UpdateProfileForm(instance=profile)

    if request.method == "POST":

        form = UpdateUserForm(request.POST, instance=request.user)

        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():

            form.save()\
            
            messages.success(request, "Username/email updated")

            return redirect('dashboard')
        
        if form_2.is_valid():

            form_2.save()

            messages.success(request, "Profile picture updated")

            return redirect('dashboard')

    context = {'form':form, 'form_2':form_2}

    return render(request, 'profile/profile-management.html', context)


# Delete account
@login_required(login_url='my-login')
def delete_account(request):

    if request.method == "POST":


        deleteUser = User.objects.get(username=request.user)

        deleteUser.delete()

        messages.success(request, "Account deleted")

        return redirect('my-login')
    
    return render(request, 'profile/delete-account.html')
