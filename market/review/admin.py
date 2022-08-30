from django.contrib import admin

from review.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'created_at')
    list_display_links = ('author', 'product')
    search_fields = ('author', 'product')


admin.site.register(Review, ReviewAdmin)
