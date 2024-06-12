from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse
from django.views import View
from .tasks import hello, printer


class IndexView(View):
    def get(self, request):
        printer.delay(10)
        hello.delay()
        return HttpResponse('Hello!')