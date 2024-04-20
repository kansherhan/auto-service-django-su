from django.shortcuts import render, HttpResponseRedirect

from .models import SparePart
from .forms import SparePartForm


def index(request):
    spare_parts_all = SparePart.objects.all()

    return render(
        request,
        "pages/spare_parts/index.html",
        context={
            "items": spare_parts_all
        }
    )


def create(request):
    if request.method == 'POST':
        form = SparePartForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = SparePartForm
    return render(request, 'pages/form.html', {'form': form})


def update(request, id):
    spare_part = SparePart.objects.get(id=id)
    if request.method == 'POST':
        form = SparePartForm(request.POST, instance=spare_part)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/spare_parts')
    else:
        form = SparePartForm(instance=spare_part)
    return render(request, 'pages/form.html', {'form': form})


def delete(request, id):
    spare_part = SparePart.objects.get(id=id)
    spare_part.delete()
    return HttpResponseRedirect('/spare_parts')
