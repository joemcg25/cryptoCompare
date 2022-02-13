from urllib import request
import json
import os
if None==os.getenv("PROJECTROOT"):
    os.environ["PROJECTROOT"]=os.getcwd()

class CryptoCompare:
    apiKey = os.getenv("API_KEY")
    baseUrl="https://min-api.cryptocompare.com"
    endpoints={"singlePrice":"/data/price"}
    def __init__(self):
        pass
    def buildURL(self):
        return self.baseUrl
    def buildAPIKeyArg(self):
        return "&api_key="+self.apiKey
    def parseArgs(self,args):
        if isinstance(args,list):
            return ",".join(args)
        return str(args)
    def createArgs(self,dict):
        empty=[]
        for i in dict.keys():
            empty.append(str(i)+"="+self.parseArgs(dict[i]))
        return "&".join(empty)
    def getPrice(self,dict):
        res=request.urlopen(self.buildURL()+"/data/price"+"?"+self.createArgs(dict))
        return json.load(res)
    def singlePrice(self,cryptoSym,refSym):
        return self.makeRequest("singlePrice",{"fsym": cryptoSym, "tsyms": refSym})
    def makeRequest(self,endpoint,args):
        if None==self.apiKey:
            return None
        res = request.urlopen(self.buildURL() + self.endpoints[endpoint] + "?" + self.createArgs(args)+self.buildAPIKeyArg())
        return json.load(res)