from django.db import models

# Create your models here.
class info(models.Model):
    full_name=models.CharField(max_length=30,verbose_name='الأســم')
    the_age=models.CharField(max_length=30,verbose_name='العمـر')
    phone_number=models.CharField(max_length=30,verbose_name='رقـم الهاتـف')
