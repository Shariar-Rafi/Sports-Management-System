from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#makemigrations means- create changes and store in a file
#migrate means- apply the pending changes created by makemigrations


# Create your models here.
# UserProfile (id, phone_number, profile_picture, address,  user_id)

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



