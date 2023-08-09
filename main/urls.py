from django.urls import path
from .views import main_page, contact_page, about_page, products_page, detiles_page, InfoUser

urlpatterns = [
    path('', main_page, name="index"),
    path("contact/", contact_page, name='contact'),
    path("about/", about_page, name='about'),
    path("catigory/<int:category>/", products_page, name='products'),
    path("product/<slug:slug>/", detiles_page, name='detiles'),
    path("user/", InfoUser.as_view(), name='userinfo')
]
