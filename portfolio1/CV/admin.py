from django.contrib import admin
from CV.models import competance,stage,formation

class CompetanceAdmin(admin.ModelAdmin):
    list_display = ('comp', 'niveau','type')
    list_filter = ('comp', 'niveau')
    search_fields = ('comp', 'type')
    ordering=('niveau',)

class stageAdmin(admin.ModelAdmin):
    list_display = ('type', 'lieu','date')
    list_filter = ('type','lieu')
    date_hierarchy = 'date'
    search_fields = ('type', 'lieu')
    ordering=('date',)


admin.site.register(competance,CompetanceAdmin)
admin.site.register(stage,stageAdmin)




