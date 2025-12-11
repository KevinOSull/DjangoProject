from .models import Comment, Game
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'name',
            'genre',
            'platform_of_choice',
            'current_status',
            'release_year',
            'hours_played',
            'game_developer'
        ]