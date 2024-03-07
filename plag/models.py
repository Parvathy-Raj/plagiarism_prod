from django.db import models

class PlagData(models.Model):
    id = models.AutoField(primary_key=True)
    plag_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_words = models.IntegerField()
    similarity_score = models.FloatField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id
    
class DomainCount(models.Model):
    
    id = models.AutoField(primary_key=True)
    domain = models.CharField(max_length = 3)
    count = models.IntegerField()
    
    def __str__(self):
        return self.id
