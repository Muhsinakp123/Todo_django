from django.db import models

# Create your models here.


class Task(models.Model):
    
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Study', 'Study'),
        ('Other', 'Other'),
    ]


    task = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')

    def __str__(self):
        return f"{self.id}: {self.task} ({self.get_priority_display()})"
