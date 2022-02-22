from urllib import request
import os,sys,csv,json,websockets
if None==os.getenv("PROJECTROOT"):
    os.environ["PROJECTROOT"]=os.getcwd()

class CryptoStreamer:
    apiKey = os.getenv("API_KEY")
    urls = {}
    channels={}
    def __init__(self):
        for i in [ "urls.csv","channels.csv"]:
            with open(os.getenv("PROJECTROOT") + "\\" + i, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if i == "urls.csv":
                        self.urls[row[0]] = row[1]
                    elif i == "channels.csv":
                        self.channels[row[0]] = row[1]
            file.close()
    def buildURL(self):
        return self.urls["streamer"]
    def buildAPIKeyArg(self):
        return "&api_key="+self.apiKey
    def getChannel(self,channel):
        return self.channels[channel]
    def streamTrade(self,exchange,base,quote):
            return "0"+"~"+exchange+"~"+base+"~"+quote
    def __repr__(self):
        return f"Streamer Crypto Compare API\n " \
               f" Current streamer API's are  {list(self.channels.keys())}"