from django.db import models
from django.utils import timezone

class AlertRule(models.Model):
    name = models.CharField(max_length=255)
    condition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def evaluate_condition(self):
        # Placeholder for condition evaluation logic
        pass

    def __str__(self):
        return self.name
