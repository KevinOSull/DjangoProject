from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.GameListView.as_view(), name='home'),
    path('<slug:slug>/', views.game_detail, name='game_detail'),
    path('summernote/', include('django_summernote.urls')),
]