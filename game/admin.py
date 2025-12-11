'''
from django.contrib import admin
from .models import Game, Comment
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Game, GameAdmin)
admin.site.register(Comment)
'''

from django.contrib import admin
from django.utils.text import slugify
from .models import Game, Comment  


@admin.action(description='Generate slugs for selected games')
def generate_slugs(modeladmin, request, queryset):
    for game in queryset:
        if not game.slug:
            game.slug = slugify(game.name)
            game.save()

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    actions = [generate_slugs]

admin.site.register(Game, GameAdmin)
admin.site.register(Comment)

