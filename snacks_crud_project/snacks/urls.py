from django.contrib import admin
from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    SnacksListView,
    SnackDetailsView,
    SnackCreateView,
    SnackUpdateView,
    SnackDeleteView
)

urlpatterns = [
    path('',HomePageView.as_view(), name="home"),
    path('about',AboutPageView.as_view(), name="about"),
    path('snacks',SnacksListView.as_view(), name="snacks"),
    path('<int:pk>/',SnackDetailsView.as_view(), name="snack_detail"),
    path('create/',SnackCreateView.as_view(), name="snack_create"),
    path('<int:pk>/update/',SnackUpdateView.as_view(), name="snack_update"),
    path('<int:pk>/delete/',SnackDeleteView.as_view(), name="snack_delete")
]