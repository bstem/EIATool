from django.db import models

class CI(models.Model):
    name = models.CharField(max_length=60)
    site = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    address = models.TextField()
    contact_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    area = models.IntegerField()

    def __unicode__(self):
        return "{0} {1}".format(self.name, self.type)

    def __str__(self):
        return self.name


class CIDataValue(models.Model):
    ci_id = models.ForeignKey('CI')
    pub_date = models.DateField()
    capacity = models.IntegerField()
    barrels_per_day = models.IntegerField()
    sale = models.IntegerField()
    revenue = models.IntegerField()
    avg_price = models.DecimalField(max_digits=5, decimal_places=2)
    coop_density = models.DecimalField(max_digits=6, decimal_places=3)
    tri_state_waiver = models.BooleanField()
    load_size = models.IntegerField()
    wind_resource = models.TextField()
    carve_out = models.DecimalField(max_digits=6, decimal_places=3)

    def __unicode__(self):
        return "{0} {1}".format(self.ci_id, self.pub_date)

    def __str__(self):
        return self.ci_id


class State(models.Model):
    state = models.CharField(max_length=2)
    padd = models.CharField(max_length=7)
    democrat = models.DecimalField(max_digits=5, decimal_places=2)
    republican = models.DecimalField(max_digits=5, decimal_places=2)
    state_mandate = models.BooleanField()
    state_mandate_link = models.TextField()

    def __unicode__(self):
        return "{0}".format(self.state)

    def __str__(self):
        return self.state


class StateDataValue(models.Model):
    state_id = models.ForeignKey('State')
    pub_date = models.DateField()
    coal = models.DecimalField(max_digits=5, decimal_places=2)
    nat_gas = models.DecimalField(max_digits=5, decimal_places=2)
    nuclear = models.DecimalField(max_digits=5, decimal_places=2)
    hydro = models.DecimalField(max_digits=5, decimal_places=2)
    biomass = models.DecimalField(max_digits=5, decimal_places=2)
    geothermal = models.DecimalField(max_digits=5, decimal_places=2)
    solar = models.DecimalField(max_digits=5, decimal_places=2)
    wind = models.DecimalField(max_digits=5, decimal_places=2)
    petroleum = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return "{0} {1}".format(self.state_id, self.pub_date)

    def __str__(self):
        return self.state_id