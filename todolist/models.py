from django.core.exceptions import ValidationError
from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return self.title

    def clean(self):
        if self.due_date and self.timestamp and self.due_date < self.timestamp.date():
            raise ValidationError("Due Date cannot be before the Timestamp created.")

    def update_task(self, title, description, due_date, tags, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tags.set(tags)
        self.status = status
        self.save()


class Tag(models.Model):
    value = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.value
