from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=30, blank=True)
    gubun = models.CharField(max_length=100,
    choices = (
        ('공급기업', '공급기업'),
        ('수요기업', '수요기업'),
    ), blank=True)