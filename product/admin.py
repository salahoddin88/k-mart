from django.contrib import admin
from product.models import Product, ProductCategory, ProductTag, ProductVariation, ProductImage
    


# class ProductImagesInline(admin.TabularInline):
#""" Display Child Form in table format  """
#     model = ProductImage
class ProductImagesInline(admin.StackedInline):
    """ Display child form in row format  """
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "product_category", "price", "status"]
    list_filter = ["product_category"]
    search_fields = ["name"]
    inlines = (ProductImagesInline, )


admin.site.register(Product, ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "status"]
    list_filter = ["name"]
    search_fields = ["name"]


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ["name", "status"]
    list_filter = ["name"]
    search_fields = ["name"]


admin.site.register(ProductVariation, ProductVariationAdmin)


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ["name", "status"]
    list_filter = ["name"]
    search_fields = ["name"]


admin.site.register(ProductTag, ProductTagAdmin)
    
    
