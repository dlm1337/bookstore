from django.urls import path
from .views import home, records

app_name = "sales"


urlpatterns = [
    path("", home),
    path("records/", records, name="records"),
]
