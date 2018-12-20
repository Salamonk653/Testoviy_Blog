from django.contrib import admin

# Register your models here.
from main.models import Category, Teg, Posts

admin.site.register(Category)
admin.site.register(Teg)
admin.site.register(Posts)