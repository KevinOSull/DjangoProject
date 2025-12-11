from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About
# Register your models here.
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('contentField',)  

admin.site.register(About, AboutAdmin)
