from django.contrib import admin
from .models import Categories, News, Players, Products, Sponsors, Staff, Matches

# Register your models here.
admin.site.register(Categories)
admin.site.register(News)
admin.site.register(Players)
admin.site.register(Products)
admin.site.register(Sponsors)
admin.site.register(Staff)
admin.site.register(Matches)