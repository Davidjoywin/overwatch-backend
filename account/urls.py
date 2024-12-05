from django.urls import path, include

from .views import AuthView, UserView, RegisterUserView


urlpatterns = [
    path('auth', AuthView.as_view()),
    path('user/<int:id>', UserView.as_view()),
    path('register', RegisterUserView.as_view())
]