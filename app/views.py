from django.shortcuts import render

def homepage(request):
    return render(request, "home.html")


def registration(request):
    return render(request, "register.html")