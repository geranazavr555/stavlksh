from django.shortcuts import render


def codestyle(request):
    return render(request, "static_pages/codestyle.html")


def home(request):
    return render(request, "static_pages/landing.html")


def monitor2017(request):
    return render(request, "static_pages/archive_2017.html")