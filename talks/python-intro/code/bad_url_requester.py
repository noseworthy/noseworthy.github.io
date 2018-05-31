import sys, \
       urllib.request, \
       logging


class UrlRequester:

    def __init__(self, url):
        self._url = url

    def getUrl(self):
        return self._url


    def setUrl(self, url):
        self._url = url


    def openUrl(self):
        return urllib.request.urlopen(self.getUrl())


class FileWriter:

    def __init__(self, filePath):
        self._filePath = filePath

    def getFilePath(self):
        return self._filePath

    def setFilePath(self, filePath):
        self._filePath = filePath

    def writeToFile(self, data):
        fileHandle = open(self.getFilePath(), 'r')
        try:
            fileHandle.write(data)
        finally:
            fileHandle.close()


class Main:

    def __init__(self, url, filePath):
        self._urlRequester = UrlRequester(url)
        self._filePath = filePath

    def getFilePath(self):
        return self._filePath

    def setFilePath(self, filePath)
        self._filePath = filePath

    def getUrlRequester(self):
        return self._urlRequester

    def setUrlRequester(self, urlRequester):
        self._urlRequester = urlRequester


    def makeRequest(self):
        fileHandle = open(self.getFilePath(), "w")
        response = self.getUrlRequester().openUrl()

        if response.status == 200:
            data = response.read()
            fileHandle.write(data)
        else:
            logging.error("""Read of url %s failed!""" % self.getUrlRequester().getUrl())

main = Main(sys.argv[1], sys.argv[2])
main.makeRequest()
