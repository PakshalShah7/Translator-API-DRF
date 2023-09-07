"""This file contains translate model."""

from django.db import models
from django.utils.translation import gettext as _

CHOICES = (
    ('EN', _('English')),
    ('FR', _('French')),
    ('ES', _('Spanish')),
    ('ZH', _('Chinese'))
)


class Translate(models.Model):
    """
    This model will store translate details.
    """
    from_language = models.CharField(max_length=500, choices=CHOICES)
    text = models.TextField()
    to_language = models.CharField(max_length=500, choices=CHOICES)
    translation = models.TextField(null=True, blank=True, editable=False)
