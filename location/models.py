from django.db import models


class County(models.Model):
    name = models.CharField(max_length= 50)
    
    class Meta:
        ordering = ['name']
        verbose_name = "County"
        verbose_name_plural = "Counties"
    
    def __str__(self):
        return self.name

class Sub_County(models.Model):
    county = models.ForeignKey(County, on_delete= models.CASCADE)
    name = models.CharField(max_length= 50)
    
    class Meta:
        ordering = ['name']
        verbose_name = "Sub-county"
        verbose_name_plural = "Sub-counties"
    
    def __str__(self):
        return self.name

class Town(models.Model):
    county = models.ForeignKey(County, on_delete= models.CASCADE,default= 1)
    sub_county = models.ForeignKey(Sub_County, on_delete= models.CASCADE)
    name = models.CharField(max_length= 50)
    
    class Meta:
        ordering = ['name']
        verbose_name = "Town"
        verbose_name_plural = "Towns"
    
    def __str__(self):
        return self.name