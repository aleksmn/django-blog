from django.db import models

class Signup(models.Model):
    email = models.EmailField()
    timespamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
