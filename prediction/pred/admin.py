from django.contrib import admin
from .models import Clasification, InputData

# Register your models here.
class ClasificationAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('glass', 'created')
    ordering = ('created',)

class InputDataAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ('ri', 'na', 'mg', 'al', 'si', 'k', 'ca', 'ba', 'fe', 'get_glass', 'created')
    ordering = ('-created',)

    def get_glass(self, obj):
        return obj.prediction.glass

admin.site.register(Clasification, ClasificationAdmin)
admin.site.register(InputData, InputDataAdmin)