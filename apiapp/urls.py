from django.urls import path
from . import views

urlpatterns = [

    path(
        "generate/",
        views.generate_qr,
        name="generate_qr"
    ),

    path(
        "history/",
        views.qr_history,
        name="history"
    ),

    path(
        "delete/<int:pk>/",
        views.delete_qr,
        name="delete_qr"
    ),
]