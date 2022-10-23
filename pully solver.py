
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
def show_grp():
    a=clicked.get()
    if a=="Inclined Plane":
        if e5.get()=="" and e4.get()=="":
            messagebox.showinfo("info","please provide input or check select")
        else:
            y=float(e5.get())
            x=math.pow((2*y/(9.8*math.sin(float(e4.get())*3.141592653589793238/180))),0.5)
            figure1 = plt.Figure(figsize=(8.3,5), dpi=60)
            ax1 = figure1.add_subplot(111)
            bar1 = FigureCanvasTkAgg(figure1, root)
            bar1.get_tk_widget().place(x=1020,y=478)
            ax1.scatter(x,y)
            ax1.set_xlabel("time")
            ax1.set_ylabel("length")
            ax1.set_title('Time vs Length')
    else:
        if e1.get()=="" and e2.get()=="" and e6.get()=="":
            messagebox.showinfo("info","please provide input or check select")
        else:
            y=float(e6.get())
            m1=float(e1.get())
            m2=float(e2.get())
            a1=0
            if m1<m2:
                a1=((m2-m1)*9.8)/(m2+m1)
            else:
                a1=((m1-m2)*9.8)/(m2+m1)
            z=y/a1
            x=math.pow(z,0.5)
            figure1 = plt.Figure(figsize=(8.3,5), dpi=60)
            ax1 = figure1.add_subplot(111)
            bar1 = FigureCanvasTkAgg(figure1, root)
            bar1.get_tk_widget().place(x=1020,y=478)
            ax1.scatter(x,y)
            ax1.set_xlabel("time")
            ax1.set_ylabel("length")
            ax1.set_title('Time vs Length')

def view_res():
    a=clicked.get()
    if a=="Pully system":
        if e1.get()=="" or e2.get()=="":
            messagebox.showinfo("info","please provide input or check select")
        else:
            if e1.get().isnumeric() and e2.get().isnumeric():
                m1=float(e1.get())
                m2=float(e2.get())
                if m1<m2:
                    a1=((m2-m1)*9.8)/(m2+m1)
                else:
                    a1=((m1-m2)*9.8)/(m2+m1)
                t=(2*m1*m2*9.8)/(m1+m2)
                x="Accleration of the system is: "+str(a1)
                y="Tension inside the string is: "+str(t)
                t2.config(text=x,bg="white")
                t3.config(text=y,bg="white")
                t4.config(bg="white",text=''' 
Note:Accleration will happen at the direction where mass
is more.
                     ''')
            else:
                messagebox.showinfo("info","not a number")
    else:
        if e4.get()=="":
            messagebox.showinfo("info","please provide input or check select")
        else:
            if isfloat(e4.get()):
                a1=9.8*math.tan(float(e4.get())*3.141592653589793238/180)
                x1="Accletation of the block is: "+str(a1)
                t2.config(text=x1)
                t4.config(bg="white",text='''
Note:accleration does not depend on mass.Surface is frictionless.''')
            else:
                messagebox.showinfo("info","not a number")
root=Tk()
root.title("physics analyzer")
root.geometry("1600x900")
photo =ImageTk.PhotoImage(file = "logo.png")
root.iconphoto(False, photo)
f1=Frame(root,height=100,bg="grey",width=1600)
f1.place(x=0,y=0)
canva1=Canvas(root,width=1000,height=670,bg="cyan")
canva1.place(x=10,y=110)
canva1.create_oval(200,200,300,300,fill="blue")
canva1.create_oval(240,240,260,260,fill="white")
canva1.create_line(200,250,200,500,fill="black")
canva1.create_line(300,250,300,500,fill="black")
canva1.create_line(250,140,250,250,fill="black",width=3)
canva1.create_line(150,140,350,140)
canva1.create_text(50,20,text="Newton's Law")
e1=Entry(canva1,width=10)
e1.place(x=170,y=500)
canva1.create_text(190,540,text="mass1")
e2=Entry(canva1,width=10)
e2.place(x=270,y=500)
canva1.create_text(300,540,text="mass2")
canva1.create_polygon(490,240,490,440,790,440,fill="blue")
canva1.create_line(430,240,490,240,width=3)
canva1.create_rectangle(430,200,490,236,fill="black")
canva1.create_rectangle(430,240,489,440,fill="blue")
canva1.create_text(460,180,text="block")
canva1.create_text(800,40,text="Enter angle for inclined plane")
canva1.create_text(800,60,text="length of inclined plane")
e4=Entry(canva1,width=10)
e4.place(x=890,y=33)
e5=Entry(canva1,width=10)
e5.place(x=890,y=55)
canva1.create_text(65,40,text="total length of rope")
e6=Entry(canva1,width=10)
e6.place(x=140,y=33)
canva1.create_text(850,630,text='''** gravitational accleration is 9.8m/s^2
**all angle in degree
**pi is taken as 3.141592653589793238''')
options = [
    "Pully system",
    "Inclined Plane",
] 
# datatype of menu text
clicked =StringVar()
# initial menu text
clicked.set( "Pully system" )
drop =OptionMenu( f1, clicked ,*options )
drop.place(x=10,y=40)
b1=Button(f1,text="view result",command=view_res)
b1.place(x=1430,y=40)
b2=Button(f1,text="show in graph",command=show_grp)
b2.place(x=1330,y=40)
f2=Frame(root,height=350,width=500,bg="white")
f2.place(x=1020,y=110)
t1=Label(f2,text="Your result is here",font=15,fg="black")
t1.place(x=160,y=10)
t2=Label(f2,text=None,bg="white")
t2.place(x=100,y=50)
t3=Label(f2,text=None,bg="white")
t3.place(x=100,y=80)
t4=Label(f2,text=None,bg="white")
t4.place(x=100,y=110)
figure1 = plt.Figure(figsize=(8.3,5), dpi=60)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().place(x=1020,y=478)
ax1.set_xlabel("time")
ax1.set_ylabel("length")
ax1.set_title('Time vs Length')
root.mainloop()























