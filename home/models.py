from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )
    option2 = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_option2",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    test = models.BigIntegerField(
        null=True,
        blank=True,
    )
    option1 = models.ForeignKey(
        "home.DemoApp",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="homepage_option1",
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class DemoApp(models.Model):
    "Generated Model"
    user2 = models.BigIntegerField()
