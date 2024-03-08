from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # if a user get deleted then all the notes related to that user will also get deleted.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
    )


    def __str__(self):
        return self.title


