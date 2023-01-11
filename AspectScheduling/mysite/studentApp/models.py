from django.db import models

class SignUp(models.Model):
    max_students = 10
    current_students = [] 
    tags = []
    restrictions = []
    name = "No Name"
    description = "No description provided"
