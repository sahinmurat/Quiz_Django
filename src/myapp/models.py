from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name")
    
    def __str__(self):
        return self.name
    class Meta :
        verbose_name_plural = 'Categories'
    
class Quiz(models.Model):
    title = models.CharField(max_length=100, verbose_name="Quiz Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta :
        verbose_name_plural = 'Quizzes'
    