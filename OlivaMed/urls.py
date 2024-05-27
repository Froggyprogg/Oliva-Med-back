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
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from Auth.views import PasswordResetView, PasswordChangeView, LoginView, UserCreateView
from QA_Block.views import QuestionCreateView, QuestionsListView, QuestionDetailView, AnswerDetailView
from Oliva_pages.views import WorkScheduleListView, AppointmentCreateView, \
    WorkScheduleListViewWithFilter, AppointmentCreateViewWithFilter, DoctorListView, DoctorDetailView, \
    MedicalServiceListView, JobListView, JobDetailView, CreateDoctorReviewView, DoctorReviewListView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/create/', UserCreateView.as_view(), name='user-create'),
    path('api/users/login/', LoginView.as_view(), name='login'),
    path('api/users/password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('api/users/password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('api/users/logout/', LogoutView.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/questions/', QuestionsListView.as_view(), name='list_questions'),
    path("api/questions/create", QuestionCreateView.as_view(), name="create_question"),
    path("api/question/<slug:slug>/", QuestionDetailView.as_view(), name="question_detail"),
    path("api/answer/<str:question>/", AnswerDetailView.as_view(), name="answer_detail"),
    path('api/medicalservices/', MedicalServiceListView.as_view(), name='medicalservice-list'),
    path('api/doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('api/doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path("api/jobs/", JobListView.as_view(), name="job-list"),
    path("api/job/<int:pk>/", JobDetailView.as_view(), name="job-detail"),
    path("api/reviews/doctor/create", CreateDoctorReviewView.as_view(),name="create_review_doctor"),
    path("api/reviews/doctor/<int:doctor_id>", DoctorReviewListView.as_view(),name="list_doctor_review"),
    path("api/work-schedule/", WorkScheduleListView.as_view(), name="work_schedule_list"),
    path("api/appointments/", AppointmentCreateView.as_view(), name="appointment_create"),
    path("api/work-schedule-filter/", WorkScheduleListViewWithFilter.as_view(), name="work_schedule_list_filter"),
    path("api/appointments-filter/", AppointmentCreateViewWithFilter.as_view(), name="appointment_create_filter"),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]

admin.site.site_header = 'Админ-панель Олива-Мед'
admin.site.site_title = 'Олива-Мед'
