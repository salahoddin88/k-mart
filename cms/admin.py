from django.contrib import admin
from cms.models import WebsiteSetting, Slider, Blog, FAQs


class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ["title", "email", "phone"]


admin.site.register(WebsiteSetting, WebsiteSettingAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ["heading", "sub_heading", "image", "status"]
    list_filter = ["heading"]
    search_fields = ["heading"]


admin.site.register(Slider, SliderAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "status"]
    list_filter = ["title"]
    search_fields = ["title"]


admin.site.register(Blog, BlogAdmin)


class FAQsAdmin(admin.ModelAdmin):
    list_display = ["question"]
    list_filter = ["question"]
    search_fields = ["question"]


admin.site.register(FAQs, FAQsAdmin)