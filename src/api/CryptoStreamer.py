from urllib import request
import os,sys,csv,json,websockets,asyncio
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
    async def initSub(self,subArg):
        url=self.urls["streamer"] + "?" + self.buildAPIKeyArg()
        async with websockets.connect(url) as websocket:
            await websocket.send(json.dumps({
                "action": "SubAdd",
                "subs": [subArg],
            }))
            while True:
                try:
                    data = await websocket.recv()
                except websocket.ConnectionClosed:
                    break
                try:
                    data = json.loads(data)
                    print(json.dumps(data,indent=4))
                except ValueError:
                    print(data)
    def runSub(self,subArg):
        asyncio.get_event_loop().run_until_complete(self.initSub(subArg))

    def __repr__(self):
        return f"Streamer Crypto Compare API\n " \
               f" Current streamer API's are  {list(self.channels.keys())}"