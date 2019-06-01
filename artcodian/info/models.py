from django.db import models

from ticketing import models as tm

# Create your models here.

class SceneInfo(models.Model):

    play = models.ForeignKey(
        'PlayInfo',
        on_delete = models.CASCADE,
        verbose_name='play information'
    )
    start_time = models.DateTimeField()
    runtime = models.IntegerField()
    total_seats = models.IntegerField()
    vacant_seats = models.IntegerField()

    def __str__(self):
        return self.play.title


class PlayInfo(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
