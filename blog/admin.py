from django.contrib import admin
from .models import Post

admin.site.site_header = "Blog Tweet Administration page"
admin.site.site_title = "Blog Tweet  Admin Area"
admin.site.index_title = "Welcome to Blog Tweet admin area"

admin.site.register(Post)
