from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "brand", "price", "created_at")
    list_filter = ("category", "brand")
    search_fields = ("name", "brand", "description")
    prepopulated_fields = {"slug": ("name",)}

    def thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 40px; width: auto; border-radius: 4px;">', obj.image.url)
        return "~"
    thumb.short_description = "Image"