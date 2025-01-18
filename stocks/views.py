from rest_framework import response, status, views

from .models import Stock
from .serializers import StockSerializer
from .tasks import get_stock_price


# Create your views here.
class StockPriceView(views.APIView):
    def post(self, request):
        stock_name = request.data.get("stock_name")

        print(stock_name)
        get_stock_price.delay(stock_name)

        return response.Response(
            data={"message": "Tarefa disparada com sucesso!"},
            status=status.HTTP_200_OK,
        )

    def get(self, request):
        stocks = Stock.objects.all()

        return response.Response(
            data=StockSerializer(stocks, many=True).data,
            status=status.HTTP_200_OK,
        )
