import os
if None==os.getenv("PROJECTROOT"):
    os.environ["PROJECTROOT"]=os.getcwd()

from api import CryptoCompare
base=CryptoCompare.CryptoCompare()
print(base.getPrice())

