import os

import requests
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime


def index(request):
    # return HttpResponse("<h1>Welcome to the API Index Page</h1>")
    return JsonResponse({"message": "Welcome to the API Index Page"})


@api_view(["GET", "POST"])
def current_datetime(request):
    if request.method == "GET":
        """現在の日時を返すAPIエンドポイント"""
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        return Response({"current_datetime": current_time})
    elif request.method == "POST":
        token = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")
        if not token:
            return Response({"error": "GITHUB_PERSONAL_ACCESS_TOKEN is not set"}, status=500)

        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        }
        response = requests.get("https://api.github.com/user/repos", headers=headers)

        if response.status_code != 200:
            return Response({"error": "Failed to fetch GitHub repos"}, status=response.status_code)

        repos = response.json()
        github_repos = [{"name": repo["name"], "url": repo["html_url"]} for repo in repos]

        return Response({"github_repos": github_repos})
