from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Game, Comment

# Create your views here.
class GameListView(generic.ListView):
    #model = Game
    queryset = Game.objects.all()
    template_name = "game/index.html"
    paginate_by = 6

def game_detail(request,slug):
    game = get_object_or_404(Game,slug=slug)
    return render(request, 'game/game_post.html', {'game': game},)

