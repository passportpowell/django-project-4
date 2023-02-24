from .models import UserComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ('posted_comment',)