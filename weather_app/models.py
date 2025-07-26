from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100)
    parameter = models.CharField(max_length=100)

    class Meta:
        unique_together = ("name", "parameter")

    def __str__(self):
        return f"{self.name} - {self.parameter}"


class ClimateData(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    year = models.IntegerField()
    jan = models.FloatField(null=True, blank=True)
    feb = models.FloatField(null=True, blank=True)
    mar = models.FloatField(null=True, blank=True)
    apr = models.FloatField(null=True, blank=True)
    may = models.FloatField(null=True, blank=True)
    jun = models.FloatField(null=True, blank=True)
    jul = models.FloatField(null=True, blank=True)
    aug = models.FloatField(null=True, blank=True)
    sep = models.FloatField(null=True, blank=True)
    oct = models.FloatField(null=True, blank=True)
    nov = models.FloatField(null=True, blank=True)
    dec = models.FloatField(null=True, blank=True)
    win = models.FloatField(null=True, blank=True)
    spr = models.FloatField(null=True, blank=True)
    sum = models.FloatField(null=True, blank=True)
    aut = models.FloatField(null=True, blank=True)
    ann = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"ClimateData {self.year}"


class ClimateDataSummary(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("region",)

    def __str__(self):
        return f"Summary for {self.region}"
