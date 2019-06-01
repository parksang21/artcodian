import random
import string


from django.db import models

from info.models import SceneInfo
# Create your models here.


def randomString(stringLength):
    """Generate a random string with the combination of lowercase and uppercase letters """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

class TicketsManager(models.Manager):
    def create_tickets(self, id_code, pur_date, title, scene):
        gen_code = randomString(10)
        ticket = self.create(id_code=gen_code, pur_date=pur_date, title=title, scene=scene)
        return ticket

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

    scene = models.ForeignKey(
        SceneInfo,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.id_code


    def save(self):
        self.id_code = randomString(10)
        super().save(self)
