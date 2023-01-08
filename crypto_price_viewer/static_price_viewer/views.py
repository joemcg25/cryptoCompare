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
    toData=base.getTopExchanges(exchange,"TO")["Data"]
    ## TODO = Map these properly to get a single result ##
    fromData = base.getTopExchanges(exchange, "FROM")["Data"]
    colz=["toSymbol","fromSymbol","volume"]
    ## TODO Format floats ##
    return render(request,"static_price_viewer/getTopExchanges.html",{"colz":colz,"toData":toData,"fromData":fromData,"exchange":exchange})

def singleIndexValue(request):
    index = request.GET['index']
    toData=base.singleIndexValue(index)["Data"]
    colz=["NAME","VALUE","LASTUPDATE","OPEN24HOUR","HIGH24HOUR","LOW24HOUR"]
    print(toData)
    return render(request,"static_price_viewer/singleIndexValue.html",{"colz":colz,"toData":toData,"index":index})