from .models import Comment, Event
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'content',
            'featured_image',
        ]
