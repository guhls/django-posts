from django.contrib.auth.models import User
from django.db import models


class Posts(models.Model):
    nome = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    number = models.IntegerField(
        unique=True, null=True, blank=False, default=None)
    cover = models.ImageField(
        upload_to='posts/%Y/%m-%d/', blank=True, default='')
    description = models.CharField(
        max_length=60, null=True, blank=True, default='')
    is_published = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.pk)
