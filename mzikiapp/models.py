from django.db import models

# Create your models here.
class Venue(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True)
    city = models.CharField(max_length=120,null=False)
    state = models.CharField(max_length=120,null=False)
    address = models.CharField(max_length=120,null=False)
    phone = models.CharField(max_length=120)
    genres = models.CharField #array
    facebook_link = models.URLField(max_length=500)
    image_link = models.CharField(max_length=500)
    website = models.URLField(max_length=120)
    seeking_talent = models.BooleanField
    seeking_description = models.CharField
    artists = models.ForeignKey("Artist",on_delete=models.CASCADE)
       
    def __str__(self) :
        return self.name