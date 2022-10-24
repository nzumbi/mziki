from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=120,unique=True)
    city = models.CharField(max_length=120,null=False)
    state = models.CharField(max_length=120,null=False)
    address = models.CharField(max_length=120,null=False)
    phone = models.CharField(max_length=120)
    genres = models.CharField(max_length=120)#array
    facebook_link = models.URLField(max_length=500)
    image_link = models.CharField(max_length=500)
    website = models.URLField(max_length=500)
    seeking_talent = models.BooleanField
    seeking_description = models.CharField(max_length=500)
    artists = models.ForeignKey("Artist",on_delete=models.CASCADE,related_name='+')

    class Meta:
        db_table = 'venue'
       
    def __str__(self) :
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=120,unique=True)
    city = models.CharField(max_length=120,null=False)
    state = models.CharField(max_length=120,null=False)
    phone = models.CharField(max_length=120)
    image_link = models.CharField(max_length=500)
    genres = models.CharField(max_length=120)#array
    facebook_link = models.URLField(max_length=500)
    website = models.URLField(max_length=120)
    seeking_venue = models.BooleanField()
    seeking_description = models.CharField(max_length=120)
    venue = models.ForeignKey(Venue,on_delete=models.CASCADE,related_name='+')

    class Meta:
        db_table = 'artist'

    def __str__(self) :
        return self.name

class Show(models.Model):
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE,related_name='shows')
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE,related_name='shows')
    start_time = models.DateField()

    class Meta:
        db_table = 'show'

    def __str__(self) :
        return self.name