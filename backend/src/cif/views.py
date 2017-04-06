from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# models
from .models import Cif

from .src import Parser

import datetime


def index(request):
    latest_cif_list = Cif.objects.order_by('-created')[:5]

    return render(request, 'cif/index.html', {
        'latest_cif_list': latest_cif_list,
    })


def lookup(request, cif):

    parser = Parser(cif=cif)

    if len(cif) == 9:

        data = dict(organization=parser.organization,
                    province=parser.province,
                    correlative_number=parser.correlative_number,
                    control_digit=parser.control_digit,
                    validator=parser.validator)

        c = Cif(number=cif, created=datetime.datetime.now(), modified=datetime.datetime.now(), data=data)
        c.save()

        return JsonResponse(data)

    return HttpResponse('CIF number not valid')
