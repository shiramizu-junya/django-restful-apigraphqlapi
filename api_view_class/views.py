from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class ItemView(APIView):
    def get(self, request):
        return Response({"message": "get"})

    def post(self, request):
        return Response({"message": "post"})

    def put(self, request):
        return Response({"message": "put"})

    def delete(self, request):
        return Response({"message": "delete"})

    def patch(self, request):
        return Response({"message": "patch"})
