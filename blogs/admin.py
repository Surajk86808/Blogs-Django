from django.contrib import admin
from .models import Category
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ('title','author','status','is_featured','created_at')
    search_fields = ('author','title','blog_body','status')
    
# Register your models here.
admin.site.register(Category)
admin.site.register(Blog ,BlogAdmin) 