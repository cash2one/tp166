from django.contrib import admin
from .models import Content,Category,EncodeFormat
# Register your models here.

class ContentAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','preview','published','created_date')
    list_filter = ('category','isMedia')
    list_per_page = 20
    search_fields = ('title',)

    def preview(self,obj):
        if obj.isMedia is not True:
            return "<div> %s </div>"%(obj.content)
        else:
            return "<img src='%s' />"%(obj.content)
    preview.allow_tags = True
    preview.short_description = "快照"



admin.site.register(Category)
admin.site.register(Content,ContentAdmin)
admin.site.register(EncodeFormat)
