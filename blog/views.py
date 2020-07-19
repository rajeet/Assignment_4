from django.shortcuts import render, get_object_or_404
from .models import BlogTable
# Create your views here.


def index(request):
    blog_obj = BlogTable.objects.all()

    return render(request, "blog/index.html", {'data':blog_obj})


def detail(request, blog_id):
    blog_obj = get_object_or_404(BlogTable, id=blog_id)
    print(blog_obj.blog_title)
    context = {
        "data": blog_obj
    }
    return render(request, "blog/detail.html", context)

