from django.contrib import admin
from .models import Key, Desc
    
class KeyAdmin(admin.ModelAdmin):
     fieldsets = [
        (None,               {'fields': ['key_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Key, KeyAdmin)
admin.site.register(Desc)
