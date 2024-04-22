from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import User_Forms
from .models import User

from django.http import HttpResponse
def test(request):
    return HttpResponse("Hello world!")

def tilni_tanlash(request):
    temp = loader.get_template("tilni_tanlash.html")
    return HttpResponse(temp.render())


def welcome(request):
    temp = loader.get_template("welcome.html")
    return HttpResponse(temp.render())

def sign_up(request):
    if request.method == "POST":
        form = User_Forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = User_Forms()

    context = {
        "forms": form
    }
    return render(request, "sign_up.html", context)

def sign_in(request):
    data = User.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        for i in data:
            if username == i.username and password == i.password:
                return redirect("welcome")

        else:
            return render(request, 'sign_in.html', {'error_message': 'Invalid login'})

    return render(request, "sign_in.html")


