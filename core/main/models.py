from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=30)
    email = models.EmailField(_("Email"), max_length=50)

    def __str__(self):
        return self.name
