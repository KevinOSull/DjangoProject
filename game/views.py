from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Game, Comment
from .forms import CommentForm
# Create your views here.
class GameListView(generic.ListView):
    #model = Game
    queryset = Game.objects.all()
    template_name = "game/index.html"
    paginate_by = 6

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    user_comments = game.comments.filter(user=request.user)
    comment_count = user_comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user     # match your Comment model
            comment.game = game             # match your Comment model
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted '
            )
            # reload comments after saving
            user_comments = game.comments.filter(user=request.user)
            comment_count = user_comments.count()
    else:
        comment_form = CommentForm()

    return render(request, 'game/game_post.html', {
        'game': game,
        'comments': user_comments,
        'comment_count': comment_count,
        'comment_form': comment_form
    })

