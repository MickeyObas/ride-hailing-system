from django.urls import path

from . import views 


urlpatterns = [
    path('confirm-email/<str:uid>/<str:token>/', views.confirm_email, name='confirm-email')
]