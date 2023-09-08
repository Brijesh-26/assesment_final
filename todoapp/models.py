from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    
    isDone= models.BooleanField(default= False)
    date= models.DateTimeField(auto_now_add= True)
    
    
    def __str__(self):
        return self.title[:20]
