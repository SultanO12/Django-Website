from django.contrib import admin
from .models import Catigory, Product, Order, OrderProduct

@admin.register(Catigory)
class CatigoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    fields = ['title', 'slug']
    prepopulated_fields = {"slug": ("title", )}
    search_fields = ('titile', )

@admin.register(Product)
class ProsuctAdmin(admin.ModelAdmin):
    list_display = ("title", "quantity", "description", "category", "price")
    fields = ("title", "slug", "description", 'quantity', "category", "image", "price", 'updated')
    readonly_fields = ['created', 'updated']
    prepopulated_fields = {"slug": ("title", )}
    search_fields = ('titile', "category")
    list_filter = ('created', 'updated')

admin.site.register(Order)
admin.site.register(OrderProduct)
