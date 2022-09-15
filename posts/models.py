from django.contrib.auth.models import User
from django.db import models


class Posts(models.Model):
    nome = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    cover = models.ImageField(upload_to='posts/%Y/%m-%d/', blank=False)
    description = models.CharField(max_length=60)
    is_published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.pk)
