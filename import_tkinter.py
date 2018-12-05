from Tkinter import *
master = Tk()
canvas_width = 80
canvas_height = 40
w = Canvas(master,width=canvas_width,height=canvas_height)
w.pack()
y = int(canvas_height/2)
w.create_line(0,y,canvas_width,y,fill="pink3")
mainloop()
