from django.urls import path
from .views import DepartmentDetailView, DepartmentView

urlpatterns = [
    path('', DepartmentView.as_view(), name='department-list'),
    path('department/<int:pk>', DepartmentView.as_view(), name='department-detail')


]