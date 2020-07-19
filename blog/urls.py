from django.urls import path
from .views import detail

app_name = "blog"
urlpatterns = [
    path("detail/<int:blog_id>/", detail, name="detail"),

]