from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect as redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from forms import *
import time


@login_required(login_url=reverse_lazy("login"))
def user_profile(request):
    profile = UserProfile.objects.get(user=request.user)

    return render(request, "user_profile/user_profile.html", {"profile": profile})


@login_required(login_url=reverse_lazy("login"))
def edit_user_profile(request, user_id):
    if request.method == "GET":
        user = UserProfile.objects.get(user=request.user)
        data = {'first_name': user.user.first_name, 'last_name': user.user.last_name,
                            'email': user.user.email, 'site': user.site}
        form = EditUserForm(data)
        return render(request, "user_profile/edit_user_profile.html", {"profile": user, "form": form})
    elif request.method == "POST":
        user = User.objects.get(username=request.user.username)
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.site = request.POST["site"]
        user_profile.save()
        user.save()
        return redirect(reverse("user_profile:user_profile"))


@login_required(login_url=reverse_lazy("login"))
def top_up(request):
    profile = UserProfile.objects.get(user=request.user)
    form = TopUpForm()
    if request.method == "GET":
        if request.session.has_key("visited"):
            old_time = request.session["visited"]
            if time.time() - old_time < 30:
                error = "You can't top up your account more than once per 30 seconds. Here wait %s seconds" % (30 - int(time.time() - old_time))
                profile = UserProfile.objects.get(user=request.user)
                return render(request, "user_profile/user_profile.html", {"profile": profile, "timeout": error})
            request.session["visited"] = time.time()
        return render(request, "user_profile/top_up.html", {"profile": profile, "form": form})
    elif request.method == "POST":
        request.session["visited"] = time.time()
        form = TopUpForm(request.POST)
        if int(request.POST["amount"]) > 0:
            profile = UserProfile.objects.get(user=request.user)
            profile.balance += int(request.POST["amount"])
            profile.save()
            return redirect(reverse("user_profile:user_profile"))
        else:
            return render(request, "user_profile/top_up.html", {"profile": profile, "form": form})


@login_required(login_url=reverse_lazy("login"))
def change_avatar(request):
    if request.method == "GET":
        form = AvatarForm()
        return render(request, "user_profile/change_avatar.html", { "form": form})
    elif request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            profile = UserProfile.objects.get(user=request.user)
            profile.avatar = form.cleaned_data["avatar"]
            profile.save()
            return redirect(reverse("user_profile:user_profile"))
