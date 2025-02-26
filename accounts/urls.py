from django.urls import path, include

from . import views 


urlpatterns = [
    path('', views.users_list),
    path('<str:pk>/update/', views.user_update),
    path('confirm-email/<str:uid>/<str:token>/', views.confirm_email, name='confirm-email')
]