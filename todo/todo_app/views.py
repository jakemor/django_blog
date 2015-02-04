from django.template import Context, loader
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from todo_app.models import todo_item
from django import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

def render_to_response(tmpl, data):
    t = loader.get_template(tmpl)
    c = Context(data)
    return HttpResponse(t.render(c))

class add_todo(forms.Form):
    content = forms.CharField(label='', max_length=500)

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

@csrf_exempt
def main(request):

    if not request.user.is_authenticated():
        return redirect('/login')

    if request.method == 'POST':
        print request.POST['content']
        # create a form instance and populate it with data from the request:
        form = add_todo(request.POST)
        # check whether it's valid:
        if form.is_valid():
            p = todo_item(content=form.cleaned_data["content"],created_at="2015-02-04",completed="false",owner=request.user)
            p.save()
            return HttpResponseRedirect("/home")
    else:
        form = add_todo()

    the_list = todo_item.objects.filter(user=request.user)
    return render_to_response("list.html", dict(todo_items=the_list, user=request.user, form=form))

def user_logout(request):
    logout(request)
    return redirect('/home')
