from django.contrib import admin
from location.models import County, Sub_County, Town

class CountyAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_display_links = ['name']
    #list_editable = ['name',]

admin.site.register(County, CountyAdmin)

class Sub_CountyAdmin(admin.ModelAdmin):
    list_display = ['name','county']
    #list_editable = ['county']
    #list_display_links = ['county']
    list_filter = ['county']

admin.site.register(Sub_County, Sub_CountyAdmin)

class TownAdmin(admin.ModelAdmin):
    list_display = ['name','sub_county','county']
    list_filter = ['county','sub_county']

admin.site.register(Town, TownAdmin)