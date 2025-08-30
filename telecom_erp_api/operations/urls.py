from django.urls import path
from .views import (
    OperationDetailsView, OperationListCreateView,
    OperationStatusUpdateView, OperationSummaryView
    )

urlpatterns = [
    path('', OperationListCreateView.as_view(), name='operations'),
    path('details/<int:pk>/', OperationDetailsView.as_view(), name='operations-details'),
    path('status/<int:pk>/', OperationStatusUpdateView.as_view(), name='operations-status-update'),
    path('summary/', OperationSummaryView.as_view(), name='operation-summary')
]