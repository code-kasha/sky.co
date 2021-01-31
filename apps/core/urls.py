from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("features/", views.features_page, name="features_page"),
    path("pricing/", views.pricing_page, name="pricing_page"),
]
