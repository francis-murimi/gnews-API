from tabnanny import verbose
from django.db import models
from location.models import Town
from profiles.models import LeaderProfile ,UserProfile, PastorProfile

class ChurchType(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField() 
    
    class Meta:
        ordering = ['title']
        verbose_name = "Type"
        verbose_name_plural = "Types"
    
    def __str__(self):
        return self.title

class ChurchDenomination(models.Model):
    full_title = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    description = models.TextField()
    church_type = models.ForeignKey(ChurchType,on_delete=models.PROTECT)
    head_quoters = models.ForeignKey(Town, on_delete= models.PROTECT)
    leader = models.ManyToManyField(LeaderProfile,through='DenominationLeadership',through_fields=('denomination','leader_profile'),)
    
    class Meta:
        ordering = ['title']
        verbose_name = "Denomination"
        verbose_name_plural = "Denominations"
    
    def __str__(self):
        return self.title

class DenominationLeadership(models.Model):
    denomination = models.ForeignKey(ChurchDenomination, on_delete= models.CASCADE)
    leader_profile = models.ForeignKey(LeaderProfile, on_delete= models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_on']
        verbose_name = "Denomination Leader"
        verbose_name_plural = "Denomination Leaders"
    
    def __str__(self):
        return self.denomination.title

class ChurchItem(models.Model):
    title = models.CharField(max_length=250)
    location = models.ForeignKey(Town, on_delete= models.PROTECT)
    church_denomination = models.ForeignKey(ChurchDenomination, on_delete= models.PROTECT,related_name='churches')
    pastor = models.ManyToManyField(PastorProfile,through='ChurchPastorship',through_fields=('church','pastor_profile'),)
    members = models.ManyToManyField(UserProfile,through='ChurchMembership',through_fields=('church', 'user_profile'),)
    
    class Meta:
        ordering = ['title']
        verbose_name = "Church"
        verbose_name_plural = "Churches"
    
    def __str__(self):
        return self.title

class ChurchMembership(models.Model):
    church = models.ForeignKey(ChurchItem, on_delete= models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete= models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    comment = models.TextField(blank=True)
    
    class Meta:
        ordering = ['created_on']
        verbose_name = "Church Membership"
        verbose_name_plural = "Church Memberships"
    
    def __str__(self):
        return self.church.title

class ChurchPastorship(models.Model):
    church = models.ForeignKey(ChurchItem, on_delete= models.CASCADE)
    pastor_profile = models.ForeignKey(PastorProfile, on_delete= models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_on']
        verbose_name = "Church Pastor"
        verbose_name_plural = "Church Pastors"
    
    def __str__(self):
        return self.church.title

