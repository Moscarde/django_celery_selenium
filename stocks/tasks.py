import yfinance as yf
from celery import shared_task
from stocks.models import Stock

@shared_task
def get_stock_price(stock_name):
    stock = yf.Ticker(stock_name)
    stock_info = stock.history(period="1d")
    if not stock_info.empty:
        price = stock_info['Close'].iloc[-1]
        Stock.objects.create(name=stock_name, price=price)
        return price
    else:
        return None

# get_stock_price("PETR4.SA")
