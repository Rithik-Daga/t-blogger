from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("add-blog/", views.addBlog, name="add-blog"),
    path("signup/", views.signUp, name="signup"),
    path("sign-in/", views.signIn, name="sign-in"),
    path("signout/", views.signout, name="signout"),
]
