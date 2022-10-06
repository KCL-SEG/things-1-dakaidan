from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )
    description = models.TextField(
        validators=[RegexValidator(
            regex=r'^.{0,120}$',
            message='Description must be 120 characters or less',
        )],
        blank=True,
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
