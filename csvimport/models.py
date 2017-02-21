from django.db import models

# class Municipality(models.Model):
# class RuralCoop(models.Model):
#     """
#     """
#     name = models.CharField(max_length=60)
#     state = models.CharField(max_length=2)
#     population = models.IntegerField()
#     energy_use = models.IntegerField()
#     import_date = models.DateField('date imported')
#
#     def __str__(self):
#         return self.name

class EthanolPlant(models.Model):
    # coop = models.ForeignKey(RuralCoop)
    statecode =  models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    capacity = models.IntegerField()
    bpd = models.IntegerField()
    padd = models.CharField(max_length=8)
    pub_month = models.DateField()


