from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        """This will return the first 50 chars of the text field
        in the post description"""
        return self.text[:50]