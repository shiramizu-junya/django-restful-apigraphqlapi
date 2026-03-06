from django.urls import path
from .views import ItemView, ItemDetailView

urlpatterns = [
    path("item/", ItemView.as_view(), name="item"),
    path("item/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
]
