from django.shortcuts import render
from django.views import generic
from .models import Game, Comment

# Create your views here.
class GameListView(generic.ListView):
    #model = Game
    queryset = Game.objects.all()
    template_name = "game/index.html"
    paginate_by = 6

