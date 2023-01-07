from urllib import request
import os,json,environ
env = environ.Env()
environ.Env.read_env()
from src.api import APIUtils as APIUtils
if None==os.getenv("PROJECTROOT"):
    os.environ["PROJECTROOT"]=os.getcwd()

class CryptoCompare:
    apiUtils = APIUtils.APIUtils()
    def __init__(self):
        pass
    def parseArgs(self,args):
        if isinstance(args,list):
            return ",".join(args)
        return str(args)
    def createArgs(self,dict):
        empty=[]
        for i in dict.keys():
            empty.append(str(i)+"="+self.parseArgs(dict[i]))
        return "&".join(empty)
    #List values
    def listCoins(self):
        return self.makeRequest("listCoins",{})
    #Get Prices
    def singlePrice(self,cryptoSym,refSym):
        return self.makeRequest("singlePrice",{"fsym": cryptoSym, "tsyms": refSym})
    def multiPrice(self,cryptoSym,refSym):
        return self.makeRequest("multiPrice",{"fsyms": cryptoSym, "tsyms": refSym})
    def multiPriceFull(self,cryptoSym,refSym):
        return self.makeRequest("multiPriceFull",{"fsyms": cryptoSym, "tsyms": refSym})
    def getTradingSignals(self,cryptoSym):
        return self.makeRequest("getTradingSignals",{"fsym": cryptoSym})
    def getOrderBook(self,cryptoSym,refSym):
        return self.makeRequest("getOrderBook", {"fsym": cryptoSym, "tsyms": refSym})
    def getTopExchanges(self,exchange,direction):
        return self.makeRequest("getTopExchanges", {"e":exchange,"direction":direction})
    def makeRequest(self,endpoint,args):
        if None==self.apiUtils.returnAPIKey():
            return None
        print(f"Call made to {endpoint} - Please see results")
        url=self.apiUtils.buildURL("static") + self.apiUtils.getEndpoints(endpoint) + "?" + self.createArgs(args)+self.apiUtils.buildAPIKeyArg()
        res = request.urlopen(url)
        resAsJson = json.load(res)
        return resAsJson
    def __repr__(self):
        return f"Static Crypto Compare API\n " \
               f" Current static API's are  {list(self.apiUtils.showEndpoints())}"