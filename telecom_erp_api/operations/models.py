from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Operation(models.Model):
    OPERATION_TYPES = [
        ('survey', 'Survey'),
        ('troubleshooting', 'Troubleshooting'),
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance')
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]

    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, related_name='operations')
    operation_type = models.CharField(max_length=20, choices=OPERATION_TYPES)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitted_operations')
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_operations')
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_operations')
    rejected_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='rejected_operations')
    approval_comments = models.TextField(blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_operation_type_display()} for {self.task.title}"
    
    class Meta:
        ordering = ['-created_at']
