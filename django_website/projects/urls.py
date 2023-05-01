from django.urls import path
from .views import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path('data/',my_view, name='my_view'),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
