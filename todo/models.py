from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Todo(models.Model):
    status_choices = (
        ('Completed', 'Completed'),
        ('In process', 'In process'),
        ('Failed', 'Failed')
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=status_choices, default=status_choices[1])

    def clean(self):
        if self.due_date == timezone.now() and self.status == self.status_choices[1]:
            self.status = self.status_choices[2]
            raise ValidationError("A task that is due today cannot be marked as 'Failed'.")

