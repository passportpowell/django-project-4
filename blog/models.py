from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from ckeditor.fields import RichTextField
# likes = models.ManyToManyField(User, related_name='liked_posts')
STATUS = ((0, "Draft"), (1, "Published"))


# class MyModel(models.Model):
#     my_field = RichTextField()



class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_posts", default=1)
    description = models.TextField()
    location = models.TextField()
    likes = models.ManyToManyField(User, related_name='event_likes', blank=True)
    published_date = models.DateTimeField(auto_now=True)
    event_info = models.TextField()
    event_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes()


class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"


class UserComment(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='usercomments')
    user = models.CharField(max_length=50)
    posted_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"



class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"





        
# TO FIX - IF YOU ADD SOMETHING OR CHANGE SOMETHING YOU MUST
#MAKEMIGRATIONS AND MIGRATE
# - kept receveing error (AttributeError at /admin/blog/usercomment/add/
# 'str' object has no attribute 'username'), when trying to post a UserComment
#     - solution: checking through the code i saw that i needed to  change the 
#         user field to a foreign key to the User model




# class Post(models.Model):
#     title = models.CharField(max_length=150)
#     slug = models.CharField(max_length=150)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     body = RichTextField()
#     image = CloudinaryField('image', null=True, blank=True)
#     # content.models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#     status = models.IntegerField(choices=STATUS, default=0)

#     class Meta:
#         ordering = ['-published_date']

#     def get_absolute_url(self):
#         return reverse('post_detail', args=[self.slug])

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title
