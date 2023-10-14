from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # You can add additional fields here if needed
    # For example: profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['id']
