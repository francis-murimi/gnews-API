from django.contrib import admin
from .models import Topic, Service, Blog, Comment

class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Topic, TopicAdmin) 

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title','church','start_time','end_time','created']
    list_filter = ['church','start_time','created']
admin.site.register(Service,ServiceAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by','status','church','service','pastor','created',]
    list_filter = ['status','created', 'updated','created_by']
    list_editable = ['status']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Blog, BlogAdmin) 

class CommentAdmin(admin.ModelAdmin):
    list_display = ['created_on','active','created_by','blog']
    list_editable = ['active']
    list_filter = ['created_on','active','created_by','blog']
admin.site.register(Comment, CommentAdmin)
