from django.urls import path

from . import views


urlpatterns = [
    path('riders/', views.riders_list),
    path('drivers/', views.drivers_list),
    path('drivers/document-upload/', views.document_upload),
]