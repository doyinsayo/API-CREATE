from django.shortcuts import render
from django.http import JsonResponse

#third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    def get(self,request, *args, **kwargs):
        data = {
        'name': 'John',
        'age': 23
        }
        return Response(data)

# Create your views here.
"""def test_view(request):
    data = {
        'name': 'John',
        'age': 23
    }
    return JsonResponse(data)"""