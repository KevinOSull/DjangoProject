from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Game, Comment
from .forms import CommentForm, GameForm
from django.contrib.auth.decorators import login_required

class GameListView(generic.ListView):
    template_name = "game/index.html"
    paginate_by = 6
    login_url = '/accounts/login/'

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


@login_required(login_url='/accounts/login/')
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

def comment_edit(request, slug, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    game = get_object_or_404(Game, slug=slug)

    if comment.user != request.user:
        messages.error(request, "You are not allowed to edit this comment.")
        return redirect('game_detail', slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully!")
            return redirect('game_detail', slug=slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'game/edit_comment.html', {'form': form, 'game': game})

def comment_delete(request, slug, comment_id):
  
    game = get_object_or_404(Game, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, game=game)

    if comment.user == request.user:
        comment.delete()
        messages.success(request, "Comment deleted!")
    

    return redirect('game_detail', slug=slug)