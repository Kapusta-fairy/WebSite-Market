from django.contrib import admin
from .models import Delivery, Payment, Politics


class OtherAdmin(admin.ModelAdmin):
    list_display_links = ('title',)


admin.site.register(Politics)
admin.site.register(Delivery)
admin.site.register(Payment)
admin.site.site_header = 'Управление'
