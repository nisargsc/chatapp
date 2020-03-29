from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    from_whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_whom')
    to_whom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_whom')

    def __str__(self):
        return f'from {self.from_whom} to {self.to_whom}'