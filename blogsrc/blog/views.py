from django.shortcuts import render

from django.template import Context, loader
from django.http import HttpResponse

def render_to_response(tmpl, data):
    t = loader.get_template(tmpl)
    c = Context(data)
    return HttpResponse(t.render(c))

# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from blog.models import *

def main(request):
    """Main listing."""
    posts = Post.objects.all().order_by("createdAt")
    paginator = Paginator(posts, 2)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("list.html", dict(posts=posts, user=request.user))


def post(request, post_id):
    comments = Comment.objects.filter(postId = post_id).order_by("createdAt")
    post = Post.objects.filter(id = post_id)
    return render_to_response("list.html", dict(post = post, comments=comments, user=request.user))