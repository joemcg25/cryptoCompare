from urllib import request
import json
import os
if None==os.getenv("PROJECTROOT"):
    os.environ["PROJECTROOT"]=os.getcwd()

class CryptoCompare:
    apiKey = os.getenv("API_KEY")
    baseUrl="https://min-api.cryptocompare.com"
    def __init__(self):
        pass
    def buildURL(self):
        return self.baseUrl
    def buildAPIKeyArg(self):
        return "api_key="+self.apiKey
    def createArgs(self,dict):
        empty=""
        for i in dict.keys():
            empty=empty+"&"+str(i)+"="+str(dict[i])
        return empty
    def getPrice(self):
        print(self.createArgs({"sym":"BTC"}))
        res=request.urlopen(self.buildURL()+"/data/price?fsym=BTC&tsyms=USD,JPY,EUR"+"&"+self.buildAPIKeyArg())
        return json.load(res)