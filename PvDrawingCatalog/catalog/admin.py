from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import AssemblyDrawing, Detail, Book, Product


class BookAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Detail, MPTTModelAdmin)
admin.site.register(AssemblyDrawing, MPTTModelAdmin)
