from django.contrib import admin
from .models import ModelExample, Photo
# Register your models here.


@admin.register(ModelExample)
class ModelExampleAdmin(admin.ModelAdmin):
	pass

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
	pass