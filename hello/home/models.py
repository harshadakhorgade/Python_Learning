from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations
# models define the database
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    # to get know carfield serch model fields
    # to get ditect chages first register your models

    def __str__(self):
        return self.name
    # this function used to show name of person who enter contact details