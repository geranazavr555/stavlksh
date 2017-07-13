from django.shortcuts import render


def codestyle(request):
    return render(request, "static_pages/codestyle.html")


def home(request):
    return render(request, "static_pages/landing.html")