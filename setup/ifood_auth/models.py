from django.db import models

class AccessToken(models.Model):
    access_token = models.CharField(max_length=5000)
    token_type = models.CharField(max_length=250)
    expires_in = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return f"Access Token: {self.access_token}, Type: {self.token_type}, Expires In: {self.expires_in}"