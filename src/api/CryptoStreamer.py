from urllib import request
import os,sys,csv,json,websockets,asyncio
from src.api import APIUtils as APIUtils
if None==os.getenv("PROJECTROOT"):
    os.environ["PROJECTROOT"]=os.getcwd()

class CryptoStreamer:
    apiUtils = APIUtils.APIUtils()
    def __init__(self):
        pass
    ## Streaming functions ##
    # Intial wrapper function
    def setStream(self,streamArg,exchange,base,quote):
        subArg=self.apiUtils.getChannels(streamArg)
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
        url=self.apiUtils.getUrlWithAPIKey("streamer")
        keyz=self.apiUtils.getSchemas(streamArg)
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