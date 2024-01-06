from django.shortcuts import render, get_object_or_404
from taggit.models import Tag

from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    context = {"posts": posts}
    return render(request, "blog/post_list.html", context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    tags = Post.tags.all()
    context = {"post": post, "tags": tags}
    return render(request, "blog/post_detail.html", context)
