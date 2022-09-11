from django.contrib import admin
from.models import ChurchType, ChurchDenomination, DenominationLeadership, ChurchItem, ChurchMembership, ChurchPastorship

class ChurchTypeAdmin(admin.ModelAdmin):
    list_display = ['title']
    #list_editable = ['title']
    list_display_links = None

admin.site.register(ChurchType, ChurchTypeAdmin)


class ChurchDenominationAdmin(admin.ModelAdmin):
    list_display = ['title','church_type','head_quoters']
    list_filter = ['church_type']

admin.site.register(ChurchDenomination, ChurchDenominationAdmin)


class DenominationLeadershipAdmin(admin.ModelAdmin):
    list_display = ['denomination','leader_profile','created_on']
    list_filter = ['created_on']

admin.site.register(DenominationLeadership, DenominationLeadershipAdmin)


class ChurchItemAdmin(admin.ModelAdmin):
    list_display = ['title','location','church_denomination']
    list_filter = ['church_denomination']

admin.site.register(ChurchItem, ChurchItemAdmin)


class ChurchMembershipAdmin(admin.ModelAdmin):
    list_display =['church','user_profile','created_on']
    list_filter = ['created_on','church']

admin.site.register(ChurchMembership, ChurchMembershipAdmin)


class ChurchPastorshipAdmin(admin.ModelAdmin):
    list_display = ['church','pastor_profile','created_on']
    list_filter = ['created_on','church']

admin.site.register(ChurchPastorship, ChurchPastorshipAdmin)
