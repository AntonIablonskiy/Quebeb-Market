from django.contrib import admin
from apps.blog.models import Article, BlockCategory, Tag

admin.site.register(Article)
admin.site.register(BlockCategory)
admin.site.register(Tag)
