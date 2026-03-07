from django.urls import path
from .views import ItemModelView, ItemModelDetailView

app_name = "apiv2"

urlpatterns = [
    path("item_model/", ItemModelView.as_view(), name="item_model"),
    path("item_model/<int:pk>/", ItemModelDetailView.as_view(), name="item_model_detail"),
]
