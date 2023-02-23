from django.contrib import admin
from .models import Event, UserComment, Attendee
from django_summernote.admin import SummernoteModelAdmin

#this should register the Event model and EventAdmin class
@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    
    #prepopulated fields makes it so the slug fiel is auto filled with what's in title
    prepopulated_fields = {'slug': ('title',)}
    #adds a filter box
    list_filter = ('status', 'published_date')
    # adds a search box
    search_fields = ['title', 'content']
    # lists different categroy across top bar
    list_display = ('title', 'slug', 'status', 'published_date')
    # 
    summernote_fields = ("event_info")


@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'posted_comment', 'created_at', 'accepted')
    list_filter = ('accepted', 'created_at')
    search_fields = ('event', 'posted_comment')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Attendee)
class UserAttendee(admin.ModelAdmin):
    list_display = ('event', 'user')
    list_filter = ('event', 'user')
    search_fields = ('event', 'posted_comment')
