from django.contrib import admin

# Register your models here.

from .models import SceneInfo, PlayInfo

@admin.register(SceneInfo)
class SceneInfoAdmin(admin.ModelAdmin):
    list_display=('play', 'start_time', 'runtime', 'total_seats', 'vacant_seats')
    pass


@admin.register(PlayInfo)
class PlayInfoAdmin(admin.ModelAdmin):
    pass
