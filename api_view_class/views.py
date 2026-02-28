from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ItemSerializer


# Create your views here.
class ItemView(APIView):

    serializer_class = ItemSerializer

    def get(self, request):
        return Response({"message": "get"})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        print(serializer)
        print(serializer.is_valid(raise_exception=True))
        print(serializer.errors)
        return Response({"message": "post", "errors": serializer.errors})

    def put(self, request):
        return Response({"message": "put"})

    def delete(self, request):
        return Response({"message": "delete"})

    def patch(self, request):
        return Response({"message": "patch"})
