from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['approve_events']

    def approve_events(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


class AssessorAdminSite(admin.AdminSite):
    site_header = "Assessor admin"
    site_title = "Assessor Admin Portal"
    index_title = "Welcome to Federal Bureau of Control"


assessor_admin_site = AssessorAdminSite(name='assessor-admin')


assessor_admin_site.register(Event)
assessor_admin_site.register(Comment)
