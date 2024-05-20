"""
URL configuration for OlivaMed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from QA_Block.views import QuestionCreateView, QuestionsListView, QuestionDetailView
from Oliva_pages.views import ReviewCreateView, ReviewsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('Auth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/questions', QuestionsListView.as_view(), name='list_questions'),
    path("api/questions/create", QuestionCreateView.as_view(), name="create_question"),
    path("api/questions/<slug:slug>/", QuestionDetailView.as_view(), name="question_detail"),
    path("api/reviews/create", ReviewCreateView.as_view(),name="create_review"),
    path("api/reviews/list", ReviewsListView.as_view(),name="create_review"),
]

admin.site.site_header = 'Oliva-Med Admin Panel'
admin.site.site_title = 'Oliva-Med'