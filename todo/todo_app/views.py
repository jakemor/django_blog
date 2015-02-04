from django.template import Context, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



# Create your views here.
def render_to_response(tmpl, data):
    t = loader.get_template(tmpl)
    c = Context(data)
    return HttpResponse(t.render(c))

@login_required(login_url=r'^login/$')
def main(request):
    todo_items = todo_items.objects.filter(owner = user._id) .order_by("createdAt")
    return render_to_response("todo_list.html", dict(todo_items=todo_item, user=request.user))

