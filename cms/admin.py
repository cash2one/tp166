from django.contrib import admin
from .models import Content,Category,EncodeFormat
# Register your models here.


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title','source')



admin.site.register(Category)
admin.site.register(Content,ContentAdmin)
admin.site.register(EncodeFormat)
