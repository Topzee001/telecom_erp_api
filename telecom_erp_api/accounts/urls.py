from django.urls import path
from .views import (UserRegisterView, UserProfileView,
                    RefreshView, AdminRegistrationView,
                    MeView, LogoutView, 
                    LoginView
                    )

urlpatterns = [
    # auth
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', RefreshView.as_view(),name='refresh' ),
    path('logout/', LogoutView.as_view(), name='logout'),

    # registeration
    path('register/', UserRegisterView.as_view(), name='refister'),
    path('admin/register/', AdminRegistrationView.as_view(), name='admin-register'),

    # user profile
    path('me/', MeView.as_view(), name='me'),
    path('users/<int:pk>/', UserProfileView.as_view(), name='user-detail')


]