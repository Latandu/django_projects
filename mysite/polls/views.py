from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 1fee5d8b is the polls index.")
