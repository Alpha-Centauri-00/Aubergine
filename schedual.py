import tkinter as tk

class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.hourstr=tk.StringVar(self,'10')
        self.hour = tk.Spinbox(self,from_=0,to=23,wrap=True,textvariable=self.hourstr,width=2,state="readonly")
        self.minstr=tk.StringVar(self,'30')
        self.minstr.trace("w",self.trace_var)
        self.last_value = ""
        self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.minstr,width=2,state="readonly")
        self.hour.grid()
        self.min.grid(row=0,column=1)

    def trace_var(self,*args):
        if self.last_value == "59" and self.minstr.get() == "0":
            self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
        self.last_value = self.minstr.get()

root = tk.Tk()
App(root).pack()
root.mainloop()

########selector
# from tkinter import *
# from vari import variables as va

# master = Tk()

# def display_selected(choice):
#     choice = hours.get()
#     print(choice)
#     return  str(0) + choice


# hours = StringVar(master)
# hours.set("Hours") # default value

# h = OptionMenu(master, hours,1,2,3,4,5,6,7,8,9,10,command=display_selected)

# h.pack()

# vari = StringVar()


# #vari.set(hours.get())

# mainloop()


######### examble for button wating for 3 secounds 
# import tkinter as tk
# from tkinter import ttk
# import time


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title('Tkinter after() Demo')
#         self.geometry('300x100')

#         self.style = ttk.Style(self)

#         self.button = ttk.Button(self, text='Wait 3 seconds')
#         self.button['command'] = self.start
#         self.button.pack(expand=True, ipadx=10, ipady=5)

#     def start(self):
#         self.change_button_color('red')
#         time.sleep(3)
#         self.change_button_color('black')

#     def change_button_color(self, color):
#         self.style.configure('TButton', foreground=color)


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

##########adding time as a label

# import tkinter as tk
# import time

# class App():
#     def __init__(self):
#         self.root = tk.Tk()
#         self.label = tk.Label(text="")
#         self.label.pack()
#         self.update_clock()
#         self.root.mainloop()

#     def update_clock(self):
#         now = time.strftime("%H:%M:%S")
#         self.label.configure(text=now)
#         self.root.after(1000, self.update_clock)

# app=App()