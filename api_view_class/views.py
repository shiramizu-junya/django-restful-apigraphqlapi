from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ItemSerializer
from .models import Item


# Create your views here.
class ItemView(APIView):

    serializer_class = ItemSerializer

    def get(self, request):
        items = Item.objects.all()
        serializer = self.serializer_class(items, many=True)
        return Response(
            {
                "data": serializer.data,
                "status": status.HTTP_200_OK,
                "message": "items retrieved",
            }
        )

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


class ItemDetailView(APIView):

    serializer_class = ItemSerializer

    def get(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(
                {
                    "data": None,
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "item not found",
                }
            )

        serializer = self.serializer_class(item)
        return Response(
            {
                "data": serializer.data,
                "status": status.HTTP_200_OK,
                "message": "item retrieved",
            }
        )

    def put(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(
                {
                    "data": None,
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "item not found",
                }
            )

        serializer = self.serializer_class(item, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()  # serializerのsave()は、create()かupdate()を呼び出すだけで、実際の処理はcreate()かupdate()に書くべき
            return Response(
                {
                    "data": serializer.data,
                    "status": status.HTTP_200_OK,
                    "message": "item updated",
                }
            )

        return Response(
            {
                "data": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "item update failed",
            }
        )

    def delete(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(
                {
                    "data": None,
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "item not found",
                }
            )

        item.delete()
        return Response(
            {
                "data": None,
                "status": status.HTTP_204_NO_CONTENT,
                "message": "item deleted",
            }
        )
