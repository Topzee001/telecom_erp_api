from django.urls import path
from .views import DepartmentDetailView, DepartmentView

urlpatterns = [
    path('', DepartmentView.as_view(), name='department-list'),
    path('<int:pk>/', DepartmentDetailView.as_view(), name='department-detail')


]