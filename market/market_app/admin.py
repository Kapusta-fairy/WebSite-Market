from django.contrib import admin
from .models import Products, Categories, Review, Politics, Color, Delivery, Payment, Currency


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'total_purchased')
    list_display_links = ('article',)
    search_fields = ('article', 'name')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'created_at')
    list_display_links = ('author', 'product')
    search_fields = ('author', 'product')


class OtherAdmin(admin.ModelAdmin):
    list_display_links = ('title',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Categories)
admin.site.register(Politics)
admin.site.register(Color)
admin.site.register(Delivery)
admin.site.register(Payment)
admin.site.register(Currency)
admin.site.site_header = 'Управление'
