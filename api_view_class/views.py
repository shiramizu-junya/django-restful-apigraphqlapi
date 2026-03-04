from django.shortcuts import render
from rest_framework import status
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

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED,
                    "message": "item created",
                }
            )

        return Response(
            {
                "data": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "item creation failed",
            }
        )

    def put(self, request):
        return Response({"message": "put"})

    def delete(self, request):
        return Response({"message": "delete"})

    def patch(self, request):
        return Response({"message": "patch"})
