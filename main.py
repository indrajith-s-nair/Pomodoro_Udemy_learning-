import tkinter as tk
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
seconds=0
minutes=0
cycle=0
id1=None
flag=False
label=None
popup=None
t1=None
t2=None
t3=None
t4=None
func_repeater=True
short_break_id=None
def short_break():
    global minutes,seconds
    global label
    global short_break_id
    global func_repeater
    if seconds>0:
        seconds=seconds-1
    else :
        seconds=59
        minutes=minutes-1
    if minutes==0 and seconds==0:
        func_repeater=True
        window.after_cancel(short_break_id)
        if label:
            label.destroy()
        timer()
    canvas.itemconfig(data,text=f"{minutes:02}:{seconds:02}",font=("Arial", 24),fill="blue")
    if minutes!=0 and seconds!=0:
        short_break_id=window.after(1000,short_break)

def timer():
    global seconds
    global minutes
    global id1
    global flag
    global cycle
    global label
    global popup
    global t1,t2,t3,func_repeater
    func_repeater=True
    if seconds<60:
        seconds=seconds+1
    if seconds>=60 :
        seconds=0
        minutes=minutes+1
    if minutes==WORK_MIN:
        seconds=0
        minutes=SHORT_BREAK_MIN
        cycle=cycle+1
        func_repeater=False
        if cycle==1:
            t1=canvas.create_text(50,223,text=" ✅ ",font=("Arial",20))
            window.lift()
            window.attributes("-topmost",False)
            window.focus_force()
        elif cycle==2:
            t2=canvas.create_text(100,223,text=" ✅ ",font=("Arial",20))
            window.lift()
            window.attributes("-topmost",False)
            window.focus_force()
        elif cycle==3:
            t3=canvas.create_text(150,223,text=" ✅ ",font=("Arial",20))
            window.lift()
            window.attributes("-topmost",False)
            window.focus_force()
        elif cycle==4:
            t4=canvas.create_text(200,223,text=" ✅ ",font=("Arial",20))
            window.lift()
            window.attributes("-topmost",False)
            window.focus_force()
        elif cycle==5:

            pause_function()
            popup=tk.Toplevel(window)
            popup.title("Notification")
            popup.geometry("250x270")
            popup.protocol("WM_DELETE_WINDOW", lambda: None)
            label=tk.Label(popup,text="You have success fully completed POMODORO ")
            label.pack()
            button=tk.Button(popup,text="okay",fg="black",bg="white",width=3,height=3,command=Reset2)
            button.place(x=125,y=220)

    if  flag==False:  #Make this true for Testing Click start button continuosly for increasing speed
        flag=True
        start.config(state="disabled")
    if func_repeater==False:
        window.after_cancel(id1)
        label=tk.Label(window,text="5 Minutes break ",fg="white",font=(FONT_NAME,20),bg="black")
        label.place(x=40,y=470)
        short_break()
        return
    canvas.itemconfig(data,text=f"{minutes:02}:{seconds:02}",font=("Arial", 24),fill="blue")
    id1=start.after(1000,timer)

def pause_function():
    global id1
    global flag
    if id1:
        start.after_cancel(id1)
    if flag==True:
        flag=False
        start.config(state="normal")
def Reset():
    global seconds
    global minutes
    global cycle
    global t1,t2,t3,t4
    if t1:
        canvas.delete(t1)
    if t2:
        canvas.delete(t2)
    if t3:
        canvas.delete(t3)
    if t4:
        canvas.delete(t4)
    pause_function()
    seconds=0
    minutes=0
    cycle=0
    canvas.itemconfig(data,text=f"{minutes:02}:{seconds:02}",font=("Arial", 24),fill="blue")
def Reset2():
    global popup
    Reset()
    popup.destroy()

window=tk.Tk()

window.geometry("500x500")

window.configure(bg=YELLOW)

window.title("POMODORO TECHNIQUE")

canvas=tk.Canvas(window,bg=YELLOW,width=229,height=263,highlightthickness=0)

canvas.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

photo=tk.PhotoImage(file="tomato.png")

canvas.create_image(100,111,image=photo)

data=canvas.create_text(100,111,text=f"{minutes:02}:{seconds:02}",font=("Arial", 24),fill="blue")

start=tk.Button(window,text="Start",fg="black",bg="white",width=2,height=2,command=timer)

start.place(x=50,y=400)

pause=tk.Button(window,text="Pause",fg="black",bg="white",width=2,height=2,command=pause_function)

pause.place(x=230,y=400)

Resets=tk.Button(window,text="Reset",fg="black",bg="white",width=2,height=2,command=Reset)
Resets.place(x=410,y=400)

window.mainloop()