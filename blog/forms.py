from .models import UserComment, Booking
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ('posted_comment',)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('event',)