from django.contrib import admin
from .models import Products, Categories, Review, Color, Currency


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'total_purchased')
    list_display_links = ('article',)
    prepopulated_fields = {'slug': ('name',), 'article': ('color', 'category', 'currency_char')}
    search_fields = ('article', 'name')


class CategoriesAdmin(admin.ModelAdmin):
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'created_at')
    list_display_links = ('author', 'product')
    search_fields = ('author', 'product')


class OtherAdmin(admin.ModelAdmin):
    list_display_links = ('title',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Categories)
admin.site.register(Color)
admin.site.register(Currency)
admin.site.site_header = 'Управление'
