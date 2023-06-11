from django.contrib import admin
from .models import Event, UserComment, Booking
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status",)
    search_fields = ["title", "event_info"]
    list_display = (
        "title",
        "time_date",
        "status",
    )
    summernote_fields = ("event_info",)

@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ("event", "user", "posted_comment", "created_at", "approved")
    list_filter = ("approved", "created_at")
    search_fields = ("event__title", "posted_comment")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("event", "user")
    list_filter = ("event", "user")
    search_fields = ("event__title", "user__username")
