from django.contrib import admin
from blog.models import Post,Comment
# Register your models here
class Adminpost(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('author',)
    search_fields=('id','title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}
admin.site.register(Post,Adminpost)

class Commentadmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')
admin.site.register(Comment,Commentadmin)