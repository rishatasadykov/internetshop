from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect as redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from good.models import Good
from forms import *
from models import Feedback
from user_profile.models import UserProfile
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required


class CatalogView(generic.ListView):
    template_name = "main/catalog.html"
    context_object_name = "goods"

    def get_queryset(self):
        return Good.objects.order_by("-rating")


def main(request):
    is_authenticated = False
    name = "Anonymous"
    user = False
    if request.user.is_authenticated():
        is_authenticated = True
        if request.user.first_name:
            name = request.user.first_name
        else:
            name = request.user.username
        user = UserProfile.objects.get(user=request.user)
    goods = Good.objects.all()
    return render(request, "main/main.html", {"is_authenticated": is_authenticated, "name": name, "user": user, "goods": goods})


def register(request):
    f = UserProfileForm()
    if request.user.is_authenticated():
        return redirect(reverse("main:main"))
    if request.method == "GET":
        context = {"f": f}
        return render(request, "main/register.html", context)
    elif request.method == "POST":
        username = request.POST["login"]
        password = request.POST["password"]
        email = request.POST["email"]
        currency = request.POST["currency"]
        exists = User.objects.filter(username=username)
        if exists:
            f = UserProfileForm(request.POST)
            context = {"error": "A user with that username already exists", "f": f}
            return render(request, "main/register.html", context)
        else:
            user = User.objects.create_user(username, email, password)
            user_profile = UserProfile()
            user_profile.user = user
            user_profile.user.first_name = request.POST["first_name"]
            user_profile.user.last_name = request.POST["last_name"]
            user_profile.currency = currency
            user_profile.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth_login(request, user)
            return redirect(reverse("main:main"))

    else:
        return HttpResponse("405")



def logout(request):
    auth_logout(request)
    return redirect(reverse("main:main"))


def login(request):
    if request.user.is_authenticated():
        return redirect(reverse("main:main"))

    if request.method == "GET":
        context = {}
        data = {"login": request.COOKIES["login"], "password": request.COOKIES["password"]}
        context["f"] = LoginForm(data=data)
        if "next" in request.GET:
            context["next"] = "?next=" + request.GET["next"]

        return render(request, "main/login.html", context)


    elif request.method == "POST":
        username = request.POST["login"]
        password = request.POST["password"]
        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            auth_login(request, user)
            if "next" in request.GET:
                return redirect(request.GET["next"])
            else:
                r = redirect(reverse("main:main"))
                if request.POST.has_key('remember_me'):
                    r.set_cookie(key="login", value=username, max_age=365 * 24 * 60 * 60)
                    r.set_cookie(key="password", value=password, max_age=365 * 24 * 60 * 60)
                return r
        else:
            return render(request, "main/login.html", {"error": "Incorrect login/password"})
    else:
        return HttpResponse("405")


@login_required(login_url=reverse_lazy("login"))
def feedback(request):
    if request.method == "GET":
        return render(request, "main/feedback.html")
    elif request.method == "POST":
        f = Feedback()
        user = UserProfile.objects.get(user=request.user)
        f.user = user
        f.message = request.POST["message"]
        f.save()
        return redirect(reverse("main:main"))