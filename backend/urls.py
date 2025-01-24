from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]


# from dj_rest_auth.registration.views import RegisterView
# from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import path

# urlpatterns = [
#     path("register/", RegisterView.as_view(), name="rest_register"),
#     path("login/", LoginView.as_view(), name="rest_login"),
#     path("logout/", LogoutView.as_view(), name="rest_logout"),
#     path("user/", UserDetailsView.as_view(), name="rest_user_details"),
# ]