from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    address = models.CharField(max_length=128)



class BlogTable(models.Model):
    blog_title = models.CharField(max_length=150)
    blog_data = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

