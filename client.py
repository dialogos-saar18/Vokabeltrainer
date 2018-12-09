from com.clt.dialog.client import Client
 
from javax.swing import JPanel, JFrame, JTextArea, JScrollPane
from java.awt import Color

frame = JFrame('Vokabeltrainer',
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
            size = (500, 500), 
        )
scrollpane = JScrollPane(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,
                             JScrollPane.HORIZONTAL_SCROLLBAR_NEVER)
scrollpane.preferredSize = 400, 800
scrollpane.visible = True
frame.add(scrollpane)
pnl = JPanel()
feld = JTextArea()
feld.editable = False
pnl.add(feld)
frame.add(pnl)
frame.visible = True    

 
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
        eingabe = value.getString()
        liste = eingabe.split()
        frage = liste[0]
        antwort = liste[1]
        symbol = liste[2]
        text = feld.getText()
        text = text+"\n"+frage+"\t"+antwort+"\t"+symbol
        feld.setText(text)
    def getName(self):
        return "Jython demo client"

    def error(self, throwable):
        print "error"


m = Main()
m.open(8000)


