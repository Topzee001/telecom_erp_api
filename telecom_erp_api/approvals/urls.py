# approvals/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('approvals/', views.ApprovalCreateView.as_view(), name='approval-create'),
    path('operations/<int:operation_id>/approvals/', views.OperationApprovalsListView.as_view(), name='operation-approvals'),
]