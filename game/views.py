from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Game, Comment
from .forms import CommentForm, GameForm


class GameListView(generic.ListView):
    template_name = "game/index.html"
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Game.objects.filter(user=user)
        return Game.objects.none()


  
def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)

    user_comments = game.comments.filter(user=request.user)
    comment_count = user_comments.count()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.game = game
            comment.save()
            messages.success(request, "Note added successfully!")
            return redirect('game_detail', slug=game.slug) 
    else:
        comment_form = CommentForm()

    return render(request, 'game/game_post.html', {
        'game': game,
        'comments': user_comments,
        'comment_count': comment_count,
        'comment_form': comment_form
    })



def add_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.user = request.user  
            game.save()
            messages.success(request, "Game added successfully!")
            return redirect('home')  
    else:
        form = GameForm()

    return render(request, 'game/add_game.html', {'form': form})


