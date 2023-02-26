import django.contrib.gis.db.models as models

# Create your models here.
class Censustract(models.Model):
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

    class Meta:
        managed = False
        db_table = 'censustract'
        unique_together = (('statefp', 'countyfp', 'tractce', 'blkgrpce'),)
