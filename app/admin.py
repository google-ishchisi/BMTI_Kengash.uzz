from pyexpat import model
from django.contrib import admin
from .models import *

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'izoh', 'post' )

admin.site.register(Post, PostAdmin)

# admin.site.register(Galereya)

admin.site.register(Azolar)

admin.site.register(Carusel)

admin.site.register(Comment, CommentAdmin)