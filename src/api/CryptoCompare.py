from urllib import request
import os,sys,csv,json
if None==os.getenv("PROJECTROOT"):
    os.environ["PROJECTROOT"]=os.getcwd()

class CryptoCompare:
    apiKey = os.getenv("API_KEY")
    endpoints={}
    urls={}
    def __init__(self):
        for i in ["endpoints.csv","urls.csv"]:
            with open(os.getenv("PROJECTROOT") + "/config/" +"/"+i,"r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if i=="endpoints.csv":
                        self.endpoints[row[0]]=row[1]
                    elif i=="urls.csv":
                        self.urls[row[0]] = row[1]
            file.close()
    def buildURL(self):
        return self.urls["static"]
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
    def makeRequest(self,endpoint,args):
        if None==self.apiKey:
            return None
        print(f"Call made to {endpoint} - Please see results")
        url=self.buildURL() + self.endpoints[endpoint] + "?" + self.createArgs(args)+self.buildAPIKeyArg()
        res = request.urlopen(url)
        return json.load(res)
    def __repr__(self):
        return f"Static Crypto Compare API\n " \
               f" Current static API's are  {list(self.endpoints.keys())}"