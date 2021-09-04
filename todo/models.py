from django.db import models
from users.models import CustomUser

class Time(models.Model):
    """Model definition for Time."""
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Time."""

        verbose_name = 'Time'
        verbose_name_plural = 'Times'

    # def __str__(self):
    #     """Unicode representation of Time."""
    #     return self.created_at

class Todo(Time):

    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name