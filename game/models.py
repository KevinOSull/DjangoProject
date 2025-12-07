from django.db import models
from django.contrib.auth.models import User
STATUS_CHOICES = ((0,"COMPLETED"),(1,"CURRENTLY_PLAYING"),(2,"ON_HOLD"),(3,"DROPPED"),(4,"PLAN_TO_PLAY"),(5,"NOT_PLAYED_YET"))
PLATFORM_OF_CHOICE = ((0,"PC"),(1,"PLAYSTATION 5"),(2,"PLAYSTATION 4"),(3,"XBOX SERIES X"),(4,"XBOX ONE"),(5, "NINTENDO SWITCH"),(6,"NINTEDO SWITCH 2"),(7,"PLAYSTATION VITA"),(8,"OTHER"))
GAME_GENRE = ((0,"ANY"),(1,"ACTION"),(2,"ACTION ADVENTURE"),(3,"JRPG"),(4,"RPG"),(5,"SIMULATION"),(6,"STRATEGY"),(7,"SPORTS"))
HOURS_PLAYED_CHOICES = ((0,"0-10"),(1,"10-50"),(2,"50-100"),(3,"100-200"),(4,"200+"))
# Create your models here.
class Game(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    genre = models.IntegerField(choices=GAME_GENRE,default=0)
    release_year = models.IntegerField(null=True,blank=True)
    game_developer = models.CharField(max_length=200,blank=True)
    current_status = models.IntegerField(choices=STATUS_CHOICES,default=4)
    platform_of_choice = models.IntegerField(choices=PLATFORM_OF_CHOICE,default=8)
    hours_played = models.IntegerField(choices=HOURS_PLAYED_CHOICES,default=0)

    class Meta:
        ordering = ["-release_year","name"]
    
    def __str__(self):
        return f"{self.name} ({self.release_year})"
    
class Comment(models.Model):
    game = models.ForeignKey(Game,on_delete=models.CASCADE,related_name="comments")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"Comment {self.body} by {self.user.username}"
        




    
    



