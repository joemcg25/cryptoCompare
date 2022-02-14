from urllib import request
import os,sys,csv,json
if None==os.getenv("PROJECTROOT"):
    os.environ["PROJECTROOT"]=os.getcwd()

class CryptoCompare:
    apiKey = os.getenv("API_KEY")
    baseUrl="https://min-api.cryptocompare.com"
    endpoints={}
    def __init__(self):
        with open(os.getenv("PROJECTROOT") + "\\endpoints.csv","r") as file:
            reader = csv.reader(file)
            for row in reader:
                self.endpoints[row[0]]=row[1]
        file.close()
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
    def singlePrice(self,cryptoSym,refSym):
        return self.makeRequest("singlePrice",{"fsym": cryptoSym, "tsyms": refSym})
    def multiPrice(self,cryptoSym,refSym):
        return self.makeRequest("multiPrice",{"fsyms": cryptoSym, "tsyms": refSym})
    def multiPriceFull(self,cryptoSym,refSym):
        return self.makeRequest("multiPriceFull",{"fsyms": cryptoSym, "tsyms": refSym})
    def makeRequest(self,endpoint,args):
        if None==self.apiKey:
            return None
        res = request.urlopen(self.buildURL() + self.endpoints[endpoint] + "?" + self.createArgs(args)+self.buildAPIKeyArg())
        return json.load(res)