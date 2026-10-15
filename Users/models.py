# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):

#     phone_number = models.CharField(max_length=15, )
#     country_name = models.CharField(max_length=20, )
#     address = models.TextField(blank=True)
#     city = models.CharField(max_length=50, blank=True)
    
#     # Manager ya aam user check karne ke liye
#     is_manager = models.BooleanField(default=False)

#     def __str__(self):
#         return self.username