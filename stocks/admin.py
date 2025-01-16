from django.contrib import admin

from .models import Stock


# Register your models here.
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "moment")
    search_fields = ("name",)
    list_filter = ("name",)
