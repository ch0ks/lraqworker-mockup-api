from django.contrib import admin


from .models import BlogPost, LRAQWorker

admin.site.register(BlogPost)
admin.site.register(LRAQWorker)