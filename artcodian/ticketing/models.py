from django.db import models

# Create your models here.

class Tickets(models.Model):

    '''
        identification code to check whether this
        online ticket is validate or not
    '''
    id_code = models.CharField(max_length=10)

    '''
        purchased date
    '''
    pur_date = models.DateTimeField('date purchased')

    '''
        play title
    '''
    title = models.CharField(max_length=200, null=True)
