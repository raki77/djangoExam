from django.db import models

# Create your models here.

# 클래스
class Post(models.Model) :
    title = models.CharField(max_length=30)
    content = models.TextField()    
    create_at = models.DateTimeField()
    
