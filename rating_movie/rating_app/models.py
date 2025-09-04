from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    rating = models.FloatField(null=True, blank=True)
    
    class Meta:
        db_table = "movie"
        
    def __str__(self):
        return self.title
    