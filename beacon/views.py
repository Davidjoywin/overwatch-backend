from django.shortcuts import render

from rest_framework.views import View
from rest_framework.response import Response


class index(View):
    def get(self, request):
        return Response(
            data={"name": "david"}, 
        )