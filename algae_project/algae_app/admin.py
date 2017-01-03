from django.contrib import admin
from .models import RawImage, RecallImage, LabelImage
class RawImageAdmin(admin.ModelAdmin):
	list_display=[f.name for f in RawImage._meta.fields]
	#list_editable=("priority",)
admin.site.register(RawImage, RawImageAdmin)

class RecallImageAdmin(admin.ModelAdmin):
	list_display=[f.name for f in RecallImage._meta.fields]
	#list_editable=("priority",)
admin.site.register(RecallImage, RecallImageAdmin)

class LabelImageAdmin(admin.ModelAdmin):
	list_display=[f.name for f in LabelImage._meta.fields]
	#list_editable=("priority",)
admin.site.register(LabelImage, LabelImageAdmin)