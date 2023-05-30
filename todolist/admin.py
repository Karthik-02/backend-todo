from django.contrib import admin
from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp', 'status', 'tag_primary_keys')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    fieldsets = (
        ('Task Details', {
            'fields': ('title', 'description', 'due_date', 'tags')
        }),
        ('Status', {
            'fields': ('status',)
        })
    )
    readonly_fields = ('timestamp',)

    def tag_primary_keys(self, obj):
        return ", ".join(str(tag.pk) for tag in obj.tags.all())

    tag_primary_keys.short_description = 'Tag Primary Keys'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
