from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("search", views.search, name="search"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("", views.index, name="listings"),
]
