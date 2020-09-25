
from django.contrib import admin
from .models import Category, Blog, SubCategory
from django.contrib.auth.models import Group

admin.site.site_header = 'Into the Charm Admin'
admin.site.unregister(Group)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'posted',)
    list_filter = ('category',)

    class Media:
        js = ('tiny.js',)

 
class CategoryAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('title',)}



class SubCategoryAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('title',)}



admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)