from django.contrib import admin

from .models import Collector, Console, VideoGame


class CollectorList(admin.ModelAdmin):
    list_display = ( 'coll_name', 'phone_number' )
    list_filter = ( 'coll_name', )
    search_fields = ('coll_name', )
    ordering = ['coll_name']


class ConsoleList(admin.ModelAdmin):
    list_display = ( 'coll_name', 'console_brand')
    list_filter = ( 'coll_name', 'console_brand')
    search_fields = ('coll_name', )
    ordering = ['coll_name']

class VideoGameList(admin.ModelAdmin):
    list_display = ( 'coll_name', 'videogame_name', )
    list_filter = ( 'coll_name', )
    search_fields = ('coll_name', )
    ordering = ['coll_name']


admin.site.register(Collector, CollectorList)
admin.site.register(Console, ConsoleList)
admin.site.register(VideoGame, VideoGameList)