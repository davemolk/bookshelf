from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404
)

from .forms import RecordForm
from .models import Record


@login_required
def record_list_view(request):
    qs = Record.objects.filter(owner=request.user)
    context = {
        'record_list': qs,
    }
    return render(request, 'records/list.html', context)


@login_required
def record_detail_view(request, slug):
    obj = get_object_or_404(Record, slug=slug, owner=request.user)
    context = {
        'record': obj,
    }
    return render(request, 'records/detail.html', context)


@login_required
def record_create_view(request):
    form = RecordForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.owner = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'records/create_update.html', context)


@login_required
def record_update_view(request, slug):
    obj = get_object_or_404(Record, slug=slug, owner=request.user) 
    form = RecordForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        'record': obj,
    }
    if form.is_valid():
        form.save()
        context['message'] = 'Save successful!'
    return render(request, 'records/create_update.html', context)