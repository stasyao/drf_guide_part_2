from django.contrib import admin

from .models import Town, Writer


admin.site.register(Town)


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    fields = ('firstname', 'patronymic', 'lastname', 'birth_place',
              'birth_date',)
    list_display = ('firstname', 'patronymic', 'lastname', 'birth_place',
                    'birth_date',)
    list_display_links = ('lastname',)
    raw_id_fields = ('birth_place', )
    ordering = ('birth_place', 'lastname', )
