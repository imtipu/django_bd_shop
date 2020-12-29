from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from django_extensions.db.fields import AutoSlugField


class Product(models.Model):
    title = models.CharField(_('Title'), max_length=500, null=False, blank=False)
    handle = AutoSlugField(populate_from='title', unique=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def slugify_function(self, content):
    #     content.replace('_', '-')
    #     return content.lower()

    def __str__(self):
        return '%s' % self.handle

    class Meta:
        ordering = ('title',)
