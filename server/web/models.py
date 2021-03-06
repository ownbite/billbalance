from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Bill(models.Model):
    amount = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)

    owner = models.ForeignKey('auth.User', related_name='bills')

    class Meta:
        ordering = ('created_date',)

class Node(models.Model):
    parentNode = models.ForeignKey('self',
                                   blank=True,
                                   null=True,
                                   related_name='subnodes')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
