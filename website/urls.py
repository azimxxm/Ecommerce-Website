from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product', views.product, name="product"),
    path('about', views.about, name="about"),
    path('card', views.card, name="card"),
]
