from django.db import models 
from django.utils.text import slugify
from django.contrib.auth.models import User
from requests import request
from church.models import ChurchItem
from profiles.models import UserProfile, PastorProfile

class Topic(models.Model):
    title = models.CharField(max_length=50,db_index=True)
    slug = models.SlugField(max_length=150,db_index=True,unique=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    church = models.ForeignKey(ChurchItem, on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('title','created',)
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
    def __str__(self): 
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Topic, self).save(*args, **kwargs)


class Service(models.Model):
    DAY_CHOICE = (
        ('sunday','Sunday'),
        ('monday','Monday'),
        ('tuesday','Tuesday'),
        ('wednesday','Wednesday'),
        ('thursday','Thursday'),
        ('friday','Friday'),
        ('saturday','Saturday'),
        ('weekend','Weekend'),
        ('weekday','Weekday'),
        ('daily','Daily'),
        ('anyday','Any Day'),
    )
    church = models.ForeignKey(ChurchItem, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    service_day = models.CharField(choices=DAY_CHOICE, max_length=15)
    start_time = models.TimeField(help_text='The time this service starts')
    end_time = models.TimeField(help_text='The time this service ends')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title


class Blog(models.Model):
    STATUS = (
        (0,"Draft"),
        (1,"Publish")
        )
    category = models.ManyToManyField(Topic,related_name='topic_blogs')
    created_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,null=True)
    service = models.ForeignKey(Service, on_delete= models.SET_NULL,null=True,related_name='service_blogs')
    church = models.ForeignKey(ChurchItem, on_delete=models.SET_NULL,null=True,related_name='church_blogs')
    pastor = models.ForeignKey(PastorProfile, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=220, db_index=True,unique=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created']
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.church = self.service.church
        super(Blog, self).save(*args, **kwargs)


class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    created_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='commentator')
    content = models.CharField(max_length= 250)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return 'Comment. {} . by {}'.format(self.content, self.created_by)