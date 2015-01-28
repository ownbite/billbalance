from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=127)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Bill(models.Model):
    person = models.ForeignKey(Person)
    amount = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ('created_date',)

    def __unicode__(self):
        return self.person.name + ' ' + str(self.amount) + ' ' + str(self.date)

