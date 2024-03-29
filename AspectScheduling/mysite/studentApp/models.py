from django.db import models
from django.utils.timezone import now
class SignUp(models.Model):
    max_students = models.IntegerField(default= 15)
    current_students = models.JSONField(default=dict)  
    tags = models.JSONField(default=dict)
    restrictions = models.JSONField(default=dict)
    name = models.TextField(default="Unamed")
    description = models.TextField(default="No description provided")
    time = models.DateTimeField(default = now)