from django.shortcuts import render
import sys,os
sys.path.insert(1, os.getcwd())
os.environ["PROJECTROOT"] = os.getcwd()+"\src"
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