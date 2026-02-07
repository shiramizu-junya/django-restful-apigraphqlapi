from django.http import HttpResponse, JsonResponse

def index(request):
    # return HttpResponse("<h1>Welcome to the API Index Page</h1>")
    return JsonResponse({"message": "Welcome to the API Index Page"})
