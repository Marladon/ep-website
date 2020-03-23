from django.http import HttpResponse


def index(request):
    return HttpResponse("EyePoint WEB Page will be here :) ")