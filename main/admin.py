from django.contrib import admin

# Register your models here.
from main.models import Category, Teg, Posts
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text_min', 'text')



admin.site.register(Category)
admin.site.register(Teg)
admin.site.register(Posts, PostAdmin)