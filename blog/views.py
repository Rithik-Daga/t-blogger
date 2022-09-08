from .models import Blog
from .forms import LoginForm, SignUpForm, AddBlogForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    p = Paginator(blogs, per_page=6)
    page_number = request.GET.get("page", 1)
    page_object = p.get_page(page_number)
    context = {"blogs": blogs, "page_object": page_object}
    return render(request, "blog/home.html", context=context)


def search(request):
    search_query = request.GET.get("search", None)
    context = {}
    if search_query:
        filtered_blogs = Blog.objects.filter(title__icontains=search_query)
        p = Paginator(filtered_blogs, per_page=6)
        page_number = request.GET.get("page", 1)
        page_object = p.get_page(page_number)
        context = {
            "filtered_blogs": filtered_blogs,
            "search_query": search_query,
            "page_object": page_object,
        }
    print(filtered_blogs, "\n\n")
    return render(request, "blog/search.html", context=context)


@login_required(login_url="sign-in")
def addBlog(request):
    form = AddBlogForm()
    if request.method == "POST":
        form = AddBlogForm(request.POST)
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        return redirect("home")
    context = {"form": form}
    return render(request, "blog/add-blog.html", context=context)


def signUp(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sign-in")
        else:
            HttpResponse("Error creating an account.")
    context = {"form": form}
    return render(request, "blog/sign-up.html", context=context)


def signIn(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            _ = User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse("User does not exist..")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("username / password is incorrect.")

    return render(request, "blog/login.html")


def signout(request):
    logout(request)
    return redirect("home")
