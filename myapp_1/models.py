from django.db import models
from django.core.exceptions import ValidationError

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    
    def clean(self):
        # Custom validation logic
        if self.name.lower() == 'admin':
            raise ValidationError('The name "admin" is not allowed.')
        if not self.email.endswith('@example.com'):
            raise ValidationError('Email must be from domain @example.com.')

    def save(self, *args, **kwargs):
        self.clean()  # Call clean method to validate
        super().save(*args, **kwargs)

