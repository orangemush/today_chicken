import json

from django.shortcuts import render
from django.views     import View
from django.http      import JsonResponse

# Create your views here.
class TestView(View):
    def get(self, request):
        return JsonResponse({'Design': 1}, status = 200)
