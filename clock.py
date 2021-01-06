import tkinter as tk
from PIL import Image,ImageTk,ImageDraw
import datetime as dt
import time
import math as m

class Clock:
    def __init__(self,root):
        self.root=root
        self.root.title("GUI Analog Clock")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="#243665")
        
        title=tk.Label(self.root,text="Analog Clock",font=("times new roman",50,"bold"),bg="#243665",fg='#8BD8BD')
        title.place(x=450,y=50)
        
        self.lbl=tk.Label(self.root,bg="black",bd=10,relief=tk.RAISED)
        self.lbl.place(x=450,y=175,height=400,width=400)
        self.working()
        
    def clock_image(self,hr_,min_,sec_):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)
        #-----For Clock Image-----------#
        bg=Image.open("images/cl.jpg")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        
        #------Formula to rotate clock pins in Anticlock Direction------#
        #angle_in_radians=angle_in_degrees*math.pi/180
        #line_length=100
        #center_x=250
        #center_y=250
        #end_x=center_x-line_length*math.cos(angle_in_radians)
        #end_y=center_y-line_length*math.sin(angle_in_radians)
        
        #------Hour Line Image----------#
        origin=200,200
        draw.line((origin,200+60*m.sin(m.radians(hr_)),200-60*m.cos(m.radians(hr_))),fill="red",width=4)
        
        #------Min Line Image----------#
        draw.line((origin,200+80*m.sin(m.radians(min_)),200-80*m.cos(m.radians(min_))),fill="blue",width=3)
        
        #------Sec Line Image----------#
        draw.line((origin,200+100*m.sin(m.radians(sec_)),200-100*m.cos(m.radians(sec_))),fill="green",width=4)
        
        draw.ellipse((191,191,210,210),fill="black")
    
        clock.save("clock_new.png")
        
    def working(self):
        h=dt.datetime.now().time().hour
        m=dt.datetime.now().time().minute
        s=dt.datetime.now().time().second
        
        hr_=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        self.clock_image(hr_,min_,sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
        
root=tk.Tk()
obj=Clock(root)
root.mainloop()