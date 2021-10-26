from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
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
    record_list = Record.objects.filter(owner=request.user)
    context = {
        'record_list': record_list,
    }
    return render(request, 'records/list.html', context)


@login_required
def record_detail_view(request, slug):
    record = get_object_or_404(Record, slug=slug, owner=request.user)
    context = {
        'record': record,
    }
    return render(request, 'records/detail.html', context)


@login_required
def record_create_view(request):
    form = RecordForm(request.POST or None)
    records = Record.objects.filter(owner=request.user)
    context = {
        'form': form,
        'records': records,
    }
    # if request.method == 'POST':
    if form.is_valid():
        obj = form.save(commit=False)
        obj.owner = request.user
        obj.save()
        # return redirect(obj.get_absolute_url())
        # return HttpResponse('Data saved\n')
        return redirect('records:detail_hx', slug=obj.slug)

    if request.htmx:
            return render(request, 'records/partials/record_form.html', context)
    return render(request, 'records/create_update.html', context)


@login_required
def record_update_view(request, slug):
    record = get_object_or_404(Record, slug=slug, owner=request.user) 
    form = RecordForm(request.POST or None, instance=record)
    context = {
        'form': form,
        'record': record,
    }
    if form.is_valid():
        form.save()
        # context['message'] = 'Save successful!'
    # if request.htmx:
    #     return render(request, 'records/partials/record_form.html', context)
    return render(request, 'records/create_update.html', context)


@login_required
def record_delete_view(request, slug):
    record = get_object_or_404(Record, slug=slug, owner=request.user)
    if request.method == 'POST':
        record.delete()
        success_url = reverse('records:list')
        return redirect(success_url)
    context = {
        'record': record
    }
    return render(request, 'records/delete.html', context)


@login_required
def create_hx(request):
    form = RecordForm()
    context = {
        'form': form,
    }
    return render(request, 'records/partials/record_form.html', context)


@login_required
def detail_hx(request, slug):
    record = get_object_or_404(Record, slug=slug, owner=request.user)
    context = {
        'record': record,
    }
    return render(request, 'records/partials/detail_hx.html', context)


@login_required
def update_hx(request, slug):
    record = get_object_or_404(Record, slug=slug, owner=request.user) 
    form = RecordForm(request.POST or None, instance=record)
    context = {
        'form': form,
        'record': record,
    }
    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.save()
    #         return redirect('records:detail_hx', slug=record.slug)
    if form.is_valid():
        form.save()
        return redirect('records:detail_hx', slug=record.slug)
    # if request.htmx:
    #     return render(request, 'records/partials/record_form.html', context)
    return render(request, 'records/partials/record_form.html', context)


@login_required
def delete_hx(request, slug):
    record = get_object_or_404(Record, slug=slug, owner=request.user)
    if request.method == 'POST':
        record.delete()
        return HttpResponse('')
