from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime


def index(request):
    # return HttpResponse("<h1>Welcome to the API Index Page</h1>")
    return JsonResponse({"message": "Welcome to the API Index Page"})


@api_view(["GET"])
def current_datetime(request):
    """現在の日時を返すAPIエンドポイント"""
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return Response({"current_datetime": current_time})
