from django.contrib.gis.db import models


# Create your models here.
class Censustract(models.Model):
    """
    test
    """

    censuscode = models.CharField(max_length=11)
    statefp = models.CharField(primary_key=True, max_length=2)
    countyfp = models.CharField(max_length=3)
    tractce = models.CharField(max_length=6)
    blkgrpce = models.CharField(max_length=2)
    affgeoid = models.CharField(max_length=21)
    geoid = models.CharField(max_length=12)
    lsad = models.CharField(max_length=2)
    aland = models.BigIntegerField()
    awater = models.BigIntegerField()
    state = models.CharField(max_length=50, blank=True, null=True)
    geometry = models.GeometryField(blank=True, null=True)
    geo_str = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "censustract"
        unique_together = (("statefp", "countyfp", "tractce", "blkgrpce"),)


class Censustract_New(models.Model):
    """
    test
    """

    censuscode = models.CharField(max_length=11)
    statefp = models.CharField(primary_key=True, max_length=2)
    countyfp = models.CharField(max_length=3)
    tractce = models.CharField(max_length=6)
    blkgrpce = models.CharField(max_length=2)
    affgeoid = models.CharField(max_length=21)
    geoid = models.CharField(max_length=12)
    lsad = models.CharField(max_length=2)
    aland = models.BigIntegerField()
    awater = models.BigIntegerField()
    state = models.CharField(max_length=50, blank=True, null=True)
    geometry = models.GeometryField(blank=True, null=True)
    geojson = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "censustract_new"
        unique_together = (("statefp", "countyfp", "tractce", "blkgrpce"),)
