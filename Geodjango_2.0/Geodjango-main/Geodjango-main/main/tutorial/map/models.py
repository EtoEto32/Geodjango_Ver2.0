# Create your models here.
#from django.db import models
from django.contrib.gis.db import models

class Evacuation(models.Model):
   evacuation_site = models.CharField(max_length=255)
   location = models.CharField(max_length=255)
   flood = models.CharField(max_length=255)
   landslides = models.CharField(max_length=255)
   storm_surge = models.CharField(max_length=255)
   earthquake = models.CharField(max_length=255)
   tsunami = models.CharField(max_length=255)
   massive_fire = models.CharField(max_length=255)
   inland_flooding = models.CharField(max_length=255)
   volcanic_phenomena = models.CharField(max_length=255)
   geom = models.PointField(srid=4326)

   def __str__(self):
       return self.evacuation_site
      