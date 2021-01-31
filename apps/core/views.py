from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import LoginForm

GITHUB_LINK = "https://github.com/code-kasha/sky.co"
DISCORD_LINK = "https://discord.gg/UADSPHcdFR"

def home_page(request):
    return render(request, 'home.html')


def features_page(request):
    context = {"github_link": GITHUB_LINK, "discord_link": DISCORD_LINK}
    return render(request, 'features.html', context)


def pricing_page(request):
    context = {"github_link": GITHUB_LINK, "discord_link": DISCORD_LINK}
    return render(request, 'pricing.html', context)


def log_in(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home_page")
    context = {"form": form}
    return render(request, "login.html", context)


def log_out(request):
    logout(request)
    return redirect("home_page")


def sign_up(request):
    pass
