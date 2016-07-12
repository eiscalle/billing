import datetime
from django.core.validators import MinValueValidator
from django.db import models

from django.utils.translation import ugettext_lazy as _


class BillingUser(models.Model):
    user_id = models.CharField(verbose_name=_('User ID'), max_length=255, primary_key=True)
    is_trial_activated = models.BooleanField(verbose_name=_('Is trial activated'), default=False, blank=True)
    payed_till = models.DateTimeField(verbose_name=_('Payed till'), null=True, default=None, blank=True)
    balance = models.DecimalField(verbose_name=_('Balance'), max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0), ], blank=True)

    def __unicode__(self):
        return self.user_id


class Order(models.Model):
    price = models.DecimalField(verbose_name=_('Price'), max_digits=6, decimal_places=2, validators=[MinValueValidator(0), ], default=0, blank=True)
    payed_from = models.DateTimeField(verbose_name=_('Payed from'), default=None, null=True, blank=True)
    payed_till = models.DateTimeField(verbose_name=_('Payed till'), default=None, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name=_('Created_at'), auto_now_add=True, blank=True)
    status = models.CharField(verbose_name=_('Status'), max_length=255, default='')
    user = models.ForeignKey(BillingUser, verbose_name=_('User'), related_name='orders')

    def __unicode__(self):
        return self.user.user_id

