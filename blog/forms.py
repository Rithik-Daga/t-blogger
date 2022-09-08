from . import models
from django import forms
from django_quill.forms import QuillFormField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        ),
    )
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        ),
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        ),
    )
    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Email", "class": "form-control"}),
    )
    password1 = forms.CharField(
        label="Password",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        ),
    )
    password2 = forms.CharField(
        label="Retype Password",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Password", "class": "form-control"}
        ),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "password"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "password"]


class BlogImageForm(forms.ModelForm):
    """
    Django ModelForm to collect property images
    of a property from the user.
    """

    class Meta:
        model = models.BlogImage
        fields = ["image"]

    def __init__(self, *args, **kwargs):
        super(BlogImageForm, self).__init__(*args, **kwargs)
        self.fields["image"].widget = forms.ClearableFileInput(
            attrs={"multiple": True, "required": False}
        )


class AddBlogForm(forms.ModelForm):

    content = QuillFormField()

    class Meta:
        model = models.Blog
        fields = ["title", "content", "summary"]

    def __init__(self, *args, **kwargs):
        super(AddBlogForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
