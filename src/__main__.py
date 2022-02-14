import os
if None==os.getenv("PROJECTROOT"):
    os.environ["PROJECTROOT"]=os.getcwd()

from api import CryptoCompare
base=CryptoCompare.CryptoCompare()
print(base.singlePrice("BTC",["USD","JPY","EUR"]))
print(base.singlePrice("ETH",["GBP"]))
print(base.multiPrice(["ETH","BTC"],["USD","JPY","EUR"]))
print(base.multiPriceFull("ETH",["GBP"]))
