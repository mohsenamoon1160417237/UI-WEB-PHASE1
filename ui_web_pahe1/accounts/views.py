import json

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login

from .models import User


def user_register(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        email = data['email']
        password = data['password']
        name = data['name']
        user, created = User.objects.get_or_create(email=email,
                                                   defaults={'first_name': name,
                                                             'password': password},
                                                   username=name)
        if created:
            user.set_password(password)

        return HttpResponseRedirect("http://127.0.0.1:8000/login/")
    else:
        return render(request, "register.html")


def user_login(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        email = data['email']
        password = data['password']
        users = User.objects.filter(email=email)
        if users.exists():
            user = users.first()
            if user.password == password:
                login(request, user=user)
                return redirect("home")
    else:
        return render(request, "Login.html")
