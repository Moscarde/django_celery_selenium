from django.urls import path

from .views import StockPriceView

urlpatterns = [path("stocks/", StockPriceView.as_view(), name="get_stock_price")]
