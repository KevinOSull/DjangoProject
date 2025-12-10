from . import views
from django.urls import path

urlpatterns = [
    path('', views.GameListView.as_view(), name='home'),
    path('<slug:slug>/', views.game_detail.as_view(), name='game_detail'),
]