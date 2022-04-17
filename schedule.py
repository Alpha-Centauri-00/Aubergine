import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, parent):
        #self.root = root
        super().__init__(parent)
        self.initialize_schedule()
        self.initialize_table()
        
    def initialize_schedule(self):
        self.hourstr=tk.StringVar(self,'10')
        self.hour = tk.Spinbox(self,from_=0,to=23,wrap=True,textvariable=self.hourstr,width=2,state="readonly")
        self.minstr=tk.StringVar(self,'30')
        self.minstr.trace("w",self.trace_var)
        self.last_value = ""
        self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.minstr,width=2,state="readonly")
        self.hour.grid()
        self.min.grid(row=0,column=1)
    
    def initialize_table(self):
        self.tree= ttk.Treeview(root, column=("c1", "c2"), show= 'headings')
        self.tree.column("# 1",anchor='center')
        self.tree.heading("# 1", text= "Jobs")
        self.tree.column("# 2", anchor= 'center')
        self.tree.heading("# 2", text= "Timeing")
        # self.tree.column("# 3", anchor= 'center')
        # self.tree.heading("# 3", text="Notes")
        self.tree.pack()
        
        AddJob_but = tk.Button(text="Add Job",command=self.adding_job)
        AddJob_but.pack()

        DelJob_but = tk.Button(text="Del Job",command=self.deleteing_job)
        DelJob_but.pack()

        test_get_value_but = tk.Button(text="get_val",command=self.get_tree_val)
        test_get_value_but.pack()
    
    def adding_job(self):
        # adding new job according to the time!
        The_Hours = self.hourstr.get()
        The_Min = self.minstr.get()
        timeing = The_Hours + ":" + The_Min
        self.tree.insert('', 'end',text= "1",values=('Every Day', timeing,""))

    def deleteing_job(self):
        # Get selected job to Delete
        if len(self.tree.selection()) == 0:
            return None
        else:
            selected_item = self.tree.selection()[0]
            self.tree.delete(selected_item)

    def trace_var(self,*args):
        if self.last_value == "59" and self.minstr.get() == "0":
            self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
        self.last_value = self.minstr.get()
    
    def get_tree_val(self):
        for line in self.tree.get_children():
            for value in self.tree.item(line)['values']:
                str1 = "Every Day"
                print(value.replace(str1,'').replace(' ','').strip())
    #             #print(type(value))
                
    #     https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter

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