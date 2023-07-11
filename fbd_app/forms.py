from .models import Comment, Event
from django import forms


# Form for creating and updating comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# Form for creating and updating events
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'content',
            'featured_image',
        ]
