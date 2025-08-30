from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Upload
from .serializers import UploadSerializer

class UploadView(generics.CreateAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
    permission_classes = [permissions.IsAuthenticated]

    # user upload for operations they submitted
    def perform_create(self, serializer):
        operation = serializer.validated_data['operation']
        if operation.submitted_by != self.request.user:
            raise PermissionDenied("You can only upload images from your own operations")
        
        serializer.save(uploaded_by=self.request.user)
                  


