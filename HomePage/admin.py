from django.contrib import admin
from django import forms
from .models import *
from nested_inline.admin import NestedModelAdmin,NestedStackedInline
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Material)