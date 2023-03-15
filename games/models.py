from django.db import models

class Games(models.Model):
    game_name = models.CharField(max_length=1000)
    game_file_link = models.CharField(max_length=1000)
    file_location = models.CharField(max_length=1000)
    game_year = models.IntegerField()
    cover = models.CharField(max_length=1000)
    file_size = models.FloatField()
    rma_file = models.FileField(upload_to='rmaFolder/', blank=True)
    rbf_file = models.FileField(upload_to='rbfFolder/', blank=True)
    def __str__(self):
        return self.game_name