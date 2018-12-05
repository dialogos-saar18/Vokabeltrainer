import import_tkinter
from com.clt.dialog.client import Client
 

class Main(Client):
    def __init__(self):
        pass

    def stateChanged(self, cs):
        print "new state: " + str(cs)

    def sessionStarted(self):
        print "session started"

    def reset(self):
        print "reset"

    def output(self, value):
        #url = "https://dict.leo.org/englisch-deutsch/dog"
        #import urllib.request
        #with urllib.request.urlopen(url) as response:
        #html = response.read()
        #with open("leoausgabe.txt","w") as f:
        #f.write(str(html))
        
        print "output: " + value.getString()
        
    def getName(self):
        return "Jython demo client"

    def error(self, throwable):
        print "error"


m = Main()
m.open(8000)


