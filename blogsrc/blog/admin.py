from django.contrib import admin
from blog.models import Post
from blog.models import Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	fields = ['title', 'body']

# give admin ability to access table
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, PostAdmin)