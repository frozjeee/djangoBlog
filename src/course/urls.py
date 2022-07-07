from django.urls import path
from .views import (
    CourseView,
    CourseCreateView,
    CourseUpdateView
)

app_name = 'courses'
urlpatterns = [
    path('', CourseView.as_view(), name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name="courses-detail"),
    path('create/', CourseCreateView.as_view(), name="courses-create"),
    path('<int:id>/update/', CourseUpdateView.as_view(), name="courses-update"),
]
