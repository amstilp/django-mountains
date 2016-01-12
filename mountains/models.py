from django.db import models
from django.conf import settings

class MountainRange(models.Model):
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=200, default="Pacific Northwest")

    def __str__(self):
        return self.name


class Mountain(models.Model):
    # static info
    name = models.CharField(max_length=200)
    height = models.PositiveIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    number_of_summits = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='mountains', null=True, blank=True)
    description = models.TextField(null=True)

    # mountain range
    mountain_range = models.ForeignKey('mountains.MountainRange', related_name='mountains', null=True)
    
    # info that can change
    snow_level = models.PositiveIntegerField(default=0)
    number_of_marmots_seen = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def see_marmot(self):
        self.number_of_marmots_seen += 1

    def snow(self, feet_of_snow):
        assert feet_of_snow > 0
        self.snow_level += feet_of_snow

    def melt(self, feet_of_snow):
        assert feet_of_snow > 0
        self.snow_level += -feet_of_snow

    def display_image(self):
        '''Return either the image of the mountain or a stock image.
        '''
        if self.image:
            return self.image.url
        else:
            return settings.STATIC_URL + "images/mountain.jpg"
