from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


def features_page(request):
    return render(request, 'features.html')


def pricing_page(request):
    return render(request, 'pricing.html')