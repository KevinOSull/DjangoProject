from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.GameListView.as_view(), name='home'),
    path('add-game/', views.add_game, name='add_game'),       # specific first
    path('<slug:slug>/', views.game_detail, name='game_detail'),  # generic last
    path('summernote/', include('django_summernote.urls')),
]
