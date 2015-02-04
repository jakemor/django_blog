from django.template import Context, loader
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from todo_app.models import todo_item

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

def render_to_response(tmpl, data):
    t = loader.get_template(tmpl)
    c = Context(data)
    return HttpResponse(t.render(c))

def main(request):
    if not request.user.is_authenticated():
        return redirect('/login')
    the_list = todo_item.objects.all()
    return render_to_response("list.html", dict(todo_items=the_list, user=request.user))

def user_logout(request):
    logout(request)
    return redirect('/home')