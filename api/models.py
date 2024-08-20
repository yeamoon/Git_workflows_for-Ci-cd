from django.db import models
from django.contrib.auth.models import User


class Notelist(models.Model):
    projectname= models.CharField(max_length=100)
    projectlist = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


    certification = models.CharField(max_length=100)
    certification_list = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self. Project_name