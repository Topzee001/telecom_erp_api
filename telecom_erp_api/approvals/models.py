# approvals/models.py
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Approval(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]
    
    operation = models.ForeignKey(
        'operations.Operation',
        on_delete=models.CASCADE,
        related_name='approvals'
    )
    reviewed_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='operation_approvals'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    comments = models.TextField(blank=True)
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Approval for {self.operation} by {self.reviewed_by}"

    class Meta:
        ordering = ['-reviewed_at']
        unique_together = ['operation', 'reviewed_by']  # One review per manager per operation