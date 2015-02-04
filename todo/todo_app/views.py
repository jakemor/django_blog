from django.template import Context, loader
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from todo_app.models import todo_item


# Create your views here.
def render_to_response(tmpl, data):
    t = loader.get_template(tmpl)
    c = Context(data)
    return HttpResponse(t.render(c))

def main(request):
    if not request.user.is_authenticated():
        return redirect('/login')
    the_list = todo_item.objects.all()
    return render_to_response("list.html", dict(todo_items=the_list, user=request.user))

