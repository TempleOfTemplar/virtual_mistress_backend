from django.contrib.auth.models import AbstractUser
from django.db import models

from api.models import Deviation, Item


class UserProfile(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/images/avatars', null=True, verbose_name="Аватар")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    deviations = models.ManyToManyField(Deviation, verbose_name="Предпочтения пользователя", related_name="user_deviation")
    items = models.ManyToManyField(Item, verbose_name="Имеющийся инвентарь инвентарь", related_name="user_item")
