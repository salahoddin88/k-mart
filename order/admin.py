from django.contrib import admin
from order.models import Order, OrderDetails


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "mobile", "payment", "status"]
    list_filter = ["user"]
    search_fields = ["user"]


admin.site.register(Order, OrderAdmin)


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "price"]
    list_filter = ["product"]
    search_fields = ["product"]


admin.site.register(OrderDetails, OrderDetailsAdmin)