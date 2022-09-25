from urllib import request
import os,sys,csv,json,websockets,asyncio
if None==os.getenv("PROJECTROOT"):
    os.environ["PROJECTROOT"]=os.getcwd()

class CryptoStreamer:
    apiKey = os.getenv("API_KEY")
    urls = {}
    channels ={}
    schemas = {}
    def __init__(self):
        for i in [ "urls.csv","channels.csv","schemas.csv"]:
            with open(os.getenv("PROJECTROOT") + "/config/" +"\\" + i, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if i == "urls.csv":
                        self.urls[row[0]] = row[1]
                    elif i == "channels.csv":
                        self.channels[row[0]] = row[1]
                    elif i == "schemas.csv":
                        self.schemas[row[0]] = row[1].split("|")
            file.close()
    def buildURL(self):
        return self.urls["streamer"]
    def buildAPIKeyArg(self):
        return "&api_key="+self.apiKey
    def getChannel(self,channel):
        return self.channels[channel]
    def extractKeys(self,channel):
        return self.schemas[channel]
    ## Streaming functions ##
    # Intial wrapper function
    def setStream(self,streamArg,exchange,base,quote):
        subArg=self.getChannel(streamArg)
        subArg=subArg.replace("{exchange}",exchange)
        subArg=subArg.replace("{base}", base)
        subArg=subArg.replace("{quote}", quote)
        self.runSub(streamArg,subArg)
    def streamTrade(self,exchange,base,quote):
        subArg=self.setStream("Trade",exchange,base,quote)
    def streamTicker(self,exchange,base,quote):
        subArg=self.setStream("Ticker",exchange,base,quote)
    def streamAggIndex(self,base,quote):
        subArg=self.setStream("AggregateIndex","CCCAGG",base,quote)
    def streamOrderBookL2(self,exchange,base,quote):
        subArg=self.setStream("OrderBookL2","CCCAGG",base,quote)
    def streamOHLCCandles(self,exchange,base,quote):
        subArg=self.setStream("OHLCCandles","CCCAGG",base,quote)
    def streamTopofOrderBook(self,exchange,base,quote):
        subArg=self.setStream("TopofOrderBook","CCCAGG",base,quote)

    ## Subscription functionality ##
    async def initSub(self,streamArg,subArg):
        url=self.urls["streamer"] + "?" + self.buildAPIKeyArg()
        keyz=self.extractKeys(streamArg)
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
                    self.parseData(keyz,data)
                except ValueError:
                    print(data)
    def parseData(self,keyz,data):
        try:
            for i in keyz:
                print(data[i])
        except KeyError:
            return
    def runSub(self,streamArg,subArg):
        asyncio.get_event_loop().run_until_complete(self.initSub(streamArg,subArg))

    def __repr__(self):
        return f"Streamer Crypto Compare API\n " \
               f" Current streamer API's are  {list(self.channels.keys())}"