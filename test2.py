from com.clt.dialog.client import Client
from javax.swing import JPanel, JFrame, JTextArea, JButton, BoxLayout, Box, JTextField
from java.awt import Color
from java.awt import Dimension



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
        t=''

        frame = JFrame('Lektion erstellen',
                    defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
                    size = (500, 500), 
                )
        def change_text(event):
            text = feld.getText()
            name = feld2.getText() + ".csv"
            with open(name,"w") as f:
                f.write(text)
                #print(name + " gespeichert")
            #print(text)
            t = text
            self.send(t)
            #return(t)

        button = JButton('Lektion speichern!', actionPerformed=change_text,size=(10,20))
        button.setBounds(20,40,20,40);
        pnl = JPanel()
        pnl.setLayout(BoxLayout(pnl, BoxLayout.Y_AXIS))
        feld = JTextArea()
        feld.editable = True

        feld.setText("Deutsch,Englisch\n")
        feld2 = JTextField()
        feld2.setText("Ersetzen durch Namen der Lektion")
        pnl.add(feld2)
        pnl.add(feld)
        pnl.add(button)
        frame.add(pnl)
        frame.setVisible(True) 

        #change_text(value)
        print(t)
        
        
        print "Lektion erstellt"


        
    def getName(self):
        return "Jython demo client"

    def error(self, throwable):
        print "error"


m = Main()
m.open(8001)


