from django.urls import path

from .views import CreateUserView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
]