from django.urls import path, include

from users.api import views


app_name = 'user'

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('profile/', views.ManageUserView.as_view(), name='profile'),
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
