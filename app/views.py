from django.shortcuts import render
from django.http import HttpResponse

stocks = [{"分類": "wow", "指數": "sss"}, {"分類": "wow", "指數": "sss"}]


# Create your views here.
def index(request):
    str1 = "<h1>hello dj</h1>"
    return HttpResponse(str1)


def get_stocks(request):
    for stock in stocks:
        print(f"{stock['分數']}-{stock['指數']}")
    return render(request, "stocks.html", {"stocks": stocks})
