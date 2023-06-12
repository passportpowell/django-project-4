from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from datetime import datetime


STATUS = ((0, "Draft"), (1, "Published"))


class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    organiser = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_posts", default=1
    )
    event_info = models.TextField()
    location = models.TextField()
    time_date = models.DateTimeField(blank=True, null=True)
    attending = models.ManyToManyField(
        User, related_name="attending_event", blank=True)
    published_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    featured_image = CloudinaryField("image", default="placeholder")

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    def attending_count(self, *, manager):
        return self.attending()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"


class UserComment(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="usercomments"
    )
    user = models.CharField(max_length=50)
    posted_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"UserComment {self.posted_comment} by {self.user}"
