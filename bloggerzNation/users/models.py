from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

# Model to control Profile
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # There is only one User for every username
    image = models.ImageField(default='/default.jpg', upload_to='profile',  # Default picture will be used if user didn't give picture
                              validators=[FileExtensionValidator(['png', 'jpg'])])

    # Returns username when trying to diplay
    def __str__(self):
        return self.user.username
