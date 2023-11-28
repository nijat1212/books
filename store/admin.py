from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin

# Register your models here.


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass


@admin.register(UserBookRelation)
class UserBookRelationAdmin(ModelAdmin):
    pass
