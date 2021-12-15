from django.urls import path, include
from .views import(
    registration_view,
    ObtainAuthTokenView,
    Logout,
    ProfileInfo,
)


app_name = 'account'

urlpatterns = [
    path('login', ObtainAuthTokenView.as_view(), name="login"),
    path('register', registration_view, name="register"),
    path('logout/',  Logout.as_view(), name="logout"),
    path('profileinfo/<int:pk>/',
         ProfileInfo.as_view(), name="profile"),
]
