from django.db import models

# Create your models here.
class Todo(models.Model):
    
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=1000)
    started_at = models.DateField() 
    ended_at = models.DateField() 

    # 作成日時、自動的に設定
    created_at = models.DateTimeField(auto_now_add=True) 
    # 更新日時、自動的に設定
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.title