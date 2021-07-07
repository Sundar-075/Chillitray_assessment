from hierarchy.views import AddView, TableView, get_view, index, show
from django.urls import path

app_name = "hierarchy"
urlpatterns = [
    path('list_view', TableView.as_view(), name="list"),
    path('add_val', AddView.as_view(), name="add"),

    path("", index, name="index"),
    path("show/", show, name="show")
]
