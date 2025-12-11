from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.GameListView.as_view(), name='home'),
    path('add-game/', views.add_game, name='add_game'),       
    path('<slug:slug>/', views.game_detail, name='game_detail'), 
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', 
     views.comment_delete, name='comment_delete'),
    path('summernote/', include('django_summernote.urls')),
]

