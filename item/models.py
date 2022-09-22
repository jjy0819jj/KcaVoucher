from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.BooleanField()
    content = models.CharField(max_length=500)
    hwp = models.CharField(max_length=100)
    hwp_progress = models.CharField(max_length=100,
                                    choices=(
                                        ('미착수', '미착수'),
                                        ('진행중', '진행중'),
                                        ('완료', '완료'),
                                    ), blank=True)
    pdf = models.CharField(max_length=100)
    pdf_progress = models.CharField(max_length=100,
                                    choices=(
                                        ('미착수', '미착수'),
                                        ('진행중', '진행중'),
                                        ('완료', '완료'),
                                    ), blank=True)
    script = models.CharField(max_length=100)
    script_progress = models.CharField(max_length=100,
                                       choices=(
                                            ('미착수', '미착수'),
                                            ('진행중', '진행중'),
                                            ('완료', '완료'),
                                       ), blank=True)