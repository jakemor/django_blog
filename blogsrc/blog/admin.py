from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	fields = ['title', 'body']

# give admin ability to access table
admin.site.register(Post, PostAdmin)