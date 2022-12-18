from django.shortcuts import render
import sys,os
sys.path.insert(1, os.getcwd())
os.environ["PROJECTROOT"] = os.getcwd()+"\src"
from src.api import CryptoCompare
# Create your views here.

# Create your views here.
base=CryptoCompare.CryptoCompare()
coins=base.listCoins()
coinSymbols=[]
for i in coins['Data'].keys():
    coinSymbols.append(i)
fiatCcys=["EUR", "USD", "GBP","JPY","CHF"]
fiatCcys.sort()

def getPrice(request):
    ccys=[]
    prices=[]
    data1=base.singlePrice("BTC",["EUR"])
    colz=["ccy","prices"]
    for i in data1.keys():
        ccys.append(i)
        prices.append(data1[i])
    return render(request,"static_price_viewer/getPrice.html",{"ccys":ccys,"prices":prices,"colz":colz})

def getCcyPrice(request):
    fiatCcy=request.GET['fiatCcy']
    cryptoCcy = request.GET['cryptoCcy']
    ccys=[]
    prices=[]
    signal=base.getTradingSignals(cryptoCcy)
    sentiment=signal["Data"]["inOutVar"]["sentiment"]
    if sentiment=="bearish":
        photo=""
    else:
        photo="{% static 'website/bullPhoto.jfif' %}"
    data=base.singlePrice(cryptoCcy,[fiatCcy])
    colz=["ccy","prices"]
    for i in data.keys():
        ccys.append(i)
        prices.append(data[i])
    return render(request,"static_price_viewer/getPrice.html",
                  {"fiatCcy":fiatCcy,"cryptoCcy":cryptoCcy,"ccys":ccys,"prices":prices,"colz":colz,
                   "fiatCcys":fiatCcys,"coinSymbols":coinSymbols,"sentiment":sentiment})
## Top Lists ##
def getTopExchanges(request):
    exchange = request.GET['exchange']
    data1=base.getTopExchanges(exchange)
    print(data1)
    return render(request,"static_price_viewer/getTopExchanges.html",{"ccys":exchange})

