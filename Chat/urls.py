from django.urls import path, include
from .views import chatPage as chat_views, logout_view
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", chat_views, name="chat-page"),
    # login-section TODO: ONLY FOR TEST. NEEDS TO BE CHANGED LATER
    path("auth/login/", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),
    path("auth/logout/", logout_view, name="logout-user"),
]