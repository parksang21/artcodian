import random
import string

from artcodian import settings
from django.db import models

from info.models import SceneInfo
# Create your models here.




class Tickets(models.Model):
    def randomString():
        """Generate a random string with the combination of lowercase and uppercase letters """
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(10))

    '''
        identification code to check whether this
        online ticket is validate or not
    '''
    id_code = models.CharField(max_length=10,
        default=randomString, unique=True)

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

    is_entered = models.BooleanField(default=False)

    qrcode_path = models.CharField(max_length=200)

    def __str__(self):
        return self.id_code
