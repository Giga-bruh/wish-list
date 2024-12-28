from django.db import models
from i_wish import settings
from django.contrib.auth.models import AbstractUser



class Polzovatel(AbstractUser):
    pass


class Zelanie(models.Model):
    polzovatel=models.ForeignKey(Polzovatel,on_delete=models.CASCADE,related_name="zelania")
    title = models.CharField(max_length=255)

    description = models.TextField()
    links = models.URLField(null=True,blank=True)
    image = models.ImageField('Изображение', upload_to='images/',
                              blank=True, null=True, default='images/default.jpg')

