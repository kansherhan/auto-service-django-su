from django.shortcuts import render

from .models import SparePart


def index(request):
    spare_parts_all = SparePart.objects.all()

    return render(
        request,
        "pages/spare_parts/index.html",
        context={
            "items": spare_parts_all
        }
    )
