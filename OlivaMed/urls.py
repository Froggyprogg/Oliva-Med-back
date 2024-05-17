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
from QA_Block import views as qa_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from QA_Block.views import QuestionCreateView
from Oliva_pages.views import ReviewCreateView, ReviewListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('Auth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('question', qa_views.list_questions, name='list_questions'),
    path("api/questions/create", QuestionCreateView.as_view(), name="create_question"),
    path("api/reviews/create", ReviewCreateView.as_view(),name="create_review"),
    path("api/reviews/list", ReviewListView.as_view(),name="create_review"),
]

admin.site.site_header = 'Oliva-Med Admin Panel'
admin.site.site_title = 'Oliva-Med'