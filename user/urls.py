from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.sign_up,name='sign_up'),
    path('signin/',views.sign_in,name='sign_in'),
    path('signout/',views.sign_out,name='sign_out'),
    path('profile/',views.profile,name='profile'),
]