from .serializers import OperationSerializer, OperationStatusUpdateSerializer, OperationCreateSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.utils import timezone
from .models import Operation
from django.db.models import Count, Q
from .permissions import canCreateOperation, CanReviewOperation


class OperationListCreateView(generics.ListCreateAPIView):
    serializer_class = OperationSerializer
    permission_classes = [permissions.IsAuthenticated, canCreateOperation]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OperationCreateSerializer
        return OperationSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role in ['ADMIN', 'MANAGER']:
            return Operation.objects.all()
        # engineers can see operations they submitted
        return Operation.objects.filter(submitted_by=user)
    
    def perform_create(self, serializer):
        task = serializer.validated_data['task']

        # engineers create opr for their task
        if(self.request.user.role == 'ENGINEER' and task.assigned_to != self.request.user):
            raise PermissionDenied("You can only create a operation report for your own task assigned")
        
        serializer.save(submitted_by=self.request.user)
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            print(f"Create error: {e}")
            raise

class OperationDetailsView(generics.RetrieveAPIView):
    queryset = Operation.objects.all()
    serializer_class= OperationSerializer
    permission_classes = [permissions.IsAuthenticated]

class OperationStatusUpdateView(generics.UpdateAPIView):
    queryset = Operation.objects.all()
    serializer_class =OperationStatusUpdateSerializer
    permission_classes= [permissions.IsAuthenticated, CanReviewOperation]

    def perform_update(self, serializer):
        operation = self.get_object()
        new_status = serializer.validated_data.get('status')
        approval_comments = serializer.validated_data.get('approval_comments')

        user = self.request.user

        if new_status == 'reviewed':
            serializer.save(reviewed_by=user, approval_comments=approval_comments)
        elif new_status == 'approved':
            serializer.save(reviewed_by=user, completed_at=timezone.now(), approval_comments=approval_comments)
        elif new_status == 'rejected':
            serializer.save(reviewed_by=user, approval_comments=approval_comments)
        else:
            serializer.save(approval_comments=approval_comments)

class OperationSummaryView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.role not in ['ADMIN', 'MANAGER']:
            return Response({"error": "Access denied"}, status=status.HTTP_403_FORBIDDEN)
        
        summary = Operation.objects.aggregate(
            total_operations=Count('id'),
            pending_operations=Count('id', filter=Q(status='pending')),
            reviewed_operations=Count('id', filter=Q(status='reviewed')),
            approved_operations=Count('id', filter=Q(status='approved')),
            rejected_operations=Count('id', filter=Q(status='rejected')),
        )

        return Response(summary)


