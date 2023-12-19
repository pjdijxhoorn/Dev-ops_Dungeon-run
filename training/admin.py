from django.contrib import admin
from .models import Training


class TrainingAdmin(admin.ModelAdmin):
    list_display = (
        'Training_name',
        'Distance',
        'Average_speed',
        'Base_score',
        'Date'
    )


ordering = ('-date',)

admin.site.register(Training, TrainingAdmin)
