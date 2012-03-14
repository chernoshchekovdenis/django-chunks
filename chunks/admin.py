from django.contrib import admin
from models import Chunk
from tinymce.widgets import TinyMCE

class ChunkAdmin(admin.ModelAdmin):
    list_display = ('key','description',)
    search_fields = ('key', 'content')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['content']:
            kwargs['widget'] = TinyMCE(attrs={'rows': 4})

        return super(ChunkAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Chunk, ChunkAdmin)
