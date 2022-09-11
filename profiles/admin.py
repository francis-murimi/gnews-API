from django.contrib import admin
from .models import UserProfile, PastorProfile, LeaderProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['profile_owner','full_name','date_of_birth','gender']
    #list_editable = ['first_name','last_lame','date_of_birth','gender']
    #list_display_links = None
    list_filter = ['gender']

admin.site.register(UserProfile,UserProfileAdmin)

class PastorProfileAdmin(admin.ModelAdmin):
    list_display = ['profile_owner','full_name','date_of_birth','gender']
    #list_editable = ['first_name','last_lame','date_of_birth','gender']
    list_filter = ['gender']

admin.site.register(PastorProfile,PastorProfileAdmin)

class LeaderProfileAdmin(admin.ModelAdmin):
    list_display = ['profile_owner','full_name','date_of_birth','gender']
    #list_editable = ['first_name','last_lame','date_of_birth','gender']
    list_filter = ['gender']

admin.site.register(LeaderProfile,LeaderProfileAdmin)