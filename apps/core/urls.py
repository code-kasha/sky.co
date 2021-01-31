from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("features/", views.features_page, name="features_page"),
    path("pricing/", views.pricing_page, name="pricing_page"),
    path("login/", views.log_in, name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.sign_up, name="signup"),
]
