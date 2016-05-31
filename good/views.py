from datetime import datetime
from django.shortcuts import render
from models import Good, Comment, Cart
from user_profile.models import UserProfile
from forms import CommentForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect as redirect


@login_required(login_url=reverse_lazy("login"))
def index(request):
    context = {'goods': Good.objects.order_by("-rating")}
    return render(request, "catalog.html", context)


@login_required(login_url=reverse_lazy("login"))
def good_page(request, good_id):
    good = Good.objects.get(id=good_id)
    comments = Comment.objects.filter(good=good)
    error = False
    f = CommentForm()
    if request.method == "GET":
        cat = good.category
        categories = cat.title
        while cat.parent:
            categories = "%s<%s" % (categories, cat.parent.title)
            cat = good.category.parent
        return render(request, "good/good.html", {'good': good, 'error': error, 'comments': comments, 'f': f,
                                                  'categories': categories})
    elif request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            cd = f.cleaned_data
            c = Comment()
            c.text = cd['text']
            c.rating = cd['rating']
            c.pub_date = datetime.now()
            c.good = Good.objects.get(id=good_id)
            c.user = UserProfile.objects.get(user=request.user)
            c.save()
            comments = Comment.objects.filter(good_id=good_id)
            sum, amount = 0, 0
            for comment in comments:
                sum += comment.rating
                amount += 1
            good.rating = int(sum/amount)
            good.save()
            return redirect(reverse("good:good_page", args=(good_id,)))
        else:
            return render(request, "good/good.html", {'good': good, 'error': error, 'comments': comments, 'f': f})
    else:
        return HttpResponse("405")


@login_required(login_url=reverse_lazy("login"))
def cart_page(request, user_id):
    if request.method == "GET":
        good_list = Cart.objects.filter(user=request.user)
        user = UserProfile.objects.get(user=request.user)
        balance = user.balance
        sum = 0
        for good in good_list:
            sum += good.good.price
        return render(request, "good/cart.html", {"good_list": good_list, "sum": sum, "balance": balance})


@login_required(login_url=reverse_lazy("login"))
def add_to_cart(request, good_id):
    good = Good.objects.raw("select * from goods where id = %s" % good_id)[0]
    cart = Cart()
    cart.user = request.user
    cart.good = good
    cart.save()
    return redirect(reverse("good:good_page", args=(good_id,)))


@login_required(login_url=reverse_lazy("login"))
def buy_goods(request):
    total_sum = 0
    goods = Cart.objects.filter(user=request.user)
    for g in goods:
        total_sum += g.good.price
    profile = UserProfile.objects.get(user=request.user)
    if profile.balance < total_sum:
        error = "You have not enough money for purchasing"
        return render(request, "good/cart.html", {"error": error, "good_list": goods})
    else:
        profile.balance -= total_sum
        profile.save()
        for g in goods:
            good = Good.objects.get(id=g.good.id)
            good.amount -= 1
            good.save()
            g.delete()
        goods = Cart.objects.filter(user=request.user)
        return render(request, "good/cart.html", {"good_list": goods})


def search(request):
    if request.method == "GET":
        return render(request, "good/search.html", {})
    elif request.method == "POST":
        context = {'goods': Good.objects.filter(title__icontains=request.POST["query"])}
        return render(request, "good/search.html", context)