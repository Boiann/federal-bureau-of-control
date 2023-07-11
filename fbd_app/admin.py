from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register the Event model with the admin site and use SummernoteModelAdmin for rich text editing
@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'approved')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['approve_events']

    # Action method to update the approved status of selected events
    def approve_events(self, request, queryset):
        queryset.update(approved=True)


# Register the Comment model with the admin site
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    # Customize the admin site headers and titles
    admin.site.site_header = "FBD Director Access"
    admin.site.site_title = "FBD Director Portal"
    admin.site.index_title = "Welcome to Federal Bureau of Control, Director"

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    # Action method to update the approved status of selected comments
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
