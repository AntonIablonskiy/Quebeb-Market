from django.contrib import admin
from apps.blog.models import Article, BlockCategory

admin.site.register(Article)
admin.site.register(BlockCategory)
