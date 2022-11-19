from django.shortcuts import render
import sys,os
sys.path.insert(1, os.getcwd())
os.environ["PROJECTROOT"] = os.getcwd()+"\src"
os.environ["API_KEY"] = "c7516cff5ec57a810759865f279f31b77f217ed35ed2f3b7650f78d25e4a3680"
from src.api import CryptoCompare

# Create your views here.
base=CryptoCompare.CryptoCompare()
coins=base.listCoins()
coinSymbols=[]
for i in coins['Data'].keys():
    coinSymbols.append(i)
ccys=["EUR", "USD", "GBP","JPY","CHF"]
ccys.sort()
def home(request):
    return render(request,"website/home.html",{"ccys":ccys,"coinSymbols":coinSymbols})