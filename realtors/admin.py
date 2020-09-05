from django.contrib import admin
from .models import Realtor

# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'is_mvp', 'hire_date')
    list_editable = ('is_mvp',)

    list_display_links = ('name', 'id')
    list_per_page = 10
    search_fields = ('name', 'is_mvp')


admin.site.register(Realtor,RealtorAdmin)