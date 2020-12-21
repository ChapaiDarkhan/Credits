from django.shortcuts import render, redirect
from django.http import HttpResponse

from credit.forms import CreditForm


def index(request):
    return HttpResponse("<h4>Hello</h4>")


def create(request):
    error = ''
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            error = form.errors
    form = CreditForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
