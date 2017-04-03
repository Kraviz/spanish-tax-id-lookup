from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .src import Parser


def index(request):
    return HttpResponse("CIF info")


def lookup(request, cif):

    parser = Parser(cif=cif)

    if len(cif) == 9:

        return JsonResponse(dict(organization=parser.organization,
                                 province=parser.province,
                                 correlative_number=parser.correlative_number,
                                 control_digit=parser.control_digit,
                                 validator=parser.validator)
                            )

    return HttpResponse('CIF number not valid')
