from django.db import models
from utils import helper_functions as hf
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Title", null=True)
    summary = models.TextField(max_length=300, verbose_name="Summary", null=True)
    content = models.TextField(max_length=2000, verbose_name="Content", null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [["author", "title"]]
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} by {self.author}"


class BlogImage(models.Model):
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=hf.getUploadPath, verbose_name="Image", null=True
    )
