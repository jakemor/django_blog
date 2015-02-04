from django.template import Context, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


# Create your views here.
def render_to_response(tmpl, data):
    t = loader.get_template(tmpl)
    c = Context(data)
    return HttpResponse(t.render(c))

def main(request):
    if not request.user.is_authenticated():
        return redirect("accounts/login")
    todo_items = todo_items.objects.filter(owner = user._id) .order_by("createdAt")

    return render_to_response("todo_list.html", dict(todo_items=todo_item, user=request.user))


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    login(request, user)