from django.urls import path
from .views import RegisterView, LogoutView, LogInView, ProfileUpdatedView, DeleteUser

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('log-in/', LogInView.as_view(), name="login"),
    path('profile-update/', ProfileUpdatedView.as_view(), name="profile-update"),
    path("delete/<int:pk>", DeleteUser.as_view(), name="delete-user"),
]