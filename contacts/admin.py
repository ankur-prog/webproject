from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('listing_id', 'listing', 'name', 'email', 'phone', 'user_id')
    list_display_links = ('listing_id', 'name')
    list_filter = ('name',)

    search_fields = ('listing_id', 'listing', 'name', 'email', 'phone', 'user_id')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
