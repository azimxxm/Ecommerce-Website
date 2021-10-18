from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product', views.product, name="product"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('accaunt', views.accaunt, name="accaunt"),
    path('card', views.card, name="card"),
    path('product_details/<str:pk>/', views.product_details, name="product_details"),
]
