import os,csv

class APIUtils:
    apiKey = os.getenv("API_KEY")
    endpoints = {}
    urls = {}
    channels = {}
    schemas = {}
    def __init__(self):
        for i in ["endpoints.csv", "urls.csv", "channels.csv", "schemas.csv"]:
            with open(os.getenv("PROJECTROOT") + "/config/" + "/" + i, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if i == "endpoints.csv":
                        self.endpoints[row[0]] = row[1]
                    elif i == "urls.csv":
                        self.urls[row[0]] = row[1]
                    elif i == "channels.csv":
                        self.channels[row[0]] = row[1]
                    elif i == "schemas.csv":
                        self.schemas[row[0]] = row[1]
            file.close()
    def returnAPIKey(self):
        return self.apiKey
    def buildURL(self,item):
        return self.urls[item]
    def buildAPIKeyArg(self):
        return "&api_key="+self.returnAPIKey()
    def getUrlWithAPIKey(self,item):
        return self.buildURL(item)+"?"+self.buildAPIKeyArg()
    def showEndpoints(self):
        return self.endpoints.keys()
    def getUrls(self,item):
        return self.urls[item]
    def getChannels(self,item):
        return self.channels[item]
    def getSchemas(self,item):
        return self.schemas[item]
    def getEndpoints(self,item):
        return self.endpoints[item]