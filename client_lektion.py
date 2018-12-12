from com.clt.dialog.client import Client
from javax.swing import JPanel, JFrame, JTextArea, JButton, BoxLayout, Box
from java.awt import Color
from java.awt import Dimension

f = open('lektion.txt','w')

frame = JFrame('Lektion erstellen',
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
            size = (500, 500), 
        )
def change_text(event):
    #f.write(feld.text)
    print(feld.text)
button = JButton('Speichern!', actionPerformed=change_text,size=(10,20))
button.setBounds(20,40,20,40);
pnl = JPanel()
pnl.setLayout(BoxLayout(pnl, BoxLayout.Y_AXIS))
feld = JTextArea()
feld.editable = True
feld.setText("Deutsch\tEnglisch\n")
pnl.add(feld)
pnl.add(button)
frame.add(pnl)
frame.setVisible(True) 


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
m.open(8001)

