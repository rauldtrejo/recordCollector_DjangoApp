from django.contrib import admin
from .models import CleaningBrush, Played, Record

# Register your models here.
admin.site.register(Record)
admin.site.register(Played)
admin.site.register(CleaningBrush)