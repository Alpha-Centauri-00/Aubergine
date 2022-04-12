import tkinter as tk
 

window = tk.Tk()
window.title('My Window')
window.geometry('100x100')
 
l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()
 
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not anything')
    else:
        l.config(text='I love both')
 
var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
 
window.mainloop()
# # import tkinter as tk
# # from tkinter import ttk
# # import glob

# # class App:
# #     def __init__(self):
# #         self.root = tk.Tk()
# #         self.tree = ttk.Treeview()
# #         self.tree.pack(side="top", fill="both")
# #         self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        

# #         ###
# #         self.tree.grid(row=0, column=0, sticky='nsew')
# #         self.btn1 = tk.Button(self.root,text = 'Run!', bd = '1',command = self.root.destroy)
# #         self.btn1.place(x=525, y=25)
# #         ###
# #         self.tree.grid(row=0,column=0,sticky='nsew')
# #         self.label1 = tk.Label(self.root,text=self.on_tree_select())
# #         self.label1.place(x=400,y=50)
# #         ###
# #         # for i in range(10):
# #         #     self.tree.insert("", "end", text="Item %s" % i)
# #         self.columns = ('first_name')

# #         tree = ttk.Treeview(self.root, columns=self.columns, show='headings')

# #         # define headings
# #         tree.heading('first_name', text='Test Cases')
# #         files = glob.glob("*.robot")
# #         contacts = []
# #         for n in files:
# #             contacts.append((f'{n}'))
# #         self.root.mainloop()

# #     def on_tree_select(self):
# #         for item in self.tree.selection():
# #             item_text = self.tree.item(item,"text")
# #             print(item_text)
# #         #return item_text
    

# # if __name__ == "__main__":
# #     app = App()

# import os
# import tkinter as tk
# import tkinter.ttk as ttk


# class App(object):
#     def __init__(self, master, path):
#         self.nodes = dict()
#         frame = tk.Frame(master)
#         self.tree = ttk.Treeview(frame)
#         ysb = ttk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
#         xsb = ttk.Scrollbar(frame, orient='horizontal', command=self.tree.xview)
#         self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
#         self.tree.heading('#0', text='Project tree', anchor='w')

#         self.tree.grid()
#         ysb.grid(row=0, column=1, sticky='ns')
#         xsb.grid(row=1, column=0, sticky='ew')
#         frame.grid()

#         abspath = os.path.abspath(path)
#         self.insert_node('', abspath, abspath)
#         self.tree.bind('<<TreeviewOpen>>', self.open_node)

#     def insert_node(self, parent, text, abspath):
#         node = self.tree.insert(parent, 'end', text=text, open=False)
#         if os.path.isdir(abspath):
#             self.nodes[node] = abspath
#             self.tree.insert(node, 'end')

#     def open_node(self, event):
#         node = self.tree.focus()
#         abspath = self.nodes.pop(node, None)
#         if abspath:
#             self.tree.delete(self.tree.get_children(node))
#             for p in os.listdir(abspath):
#                 self.insert_node(node, p, os.path.join(abspath, p))


# if __name__ == '__main__':
#     root = tk.Tk()
#     app = App(root, path='.')
#     root.mainloop()

######################################################################


# from tkinter import *
# root = Tk()
# root.title("Binding Events")
# root.geometry("400x100")
# def clicked(event):
#         label.config(text="Left button clicked")
# click = Button(root, text="Click Here", font="ariel 15 bold", bg="black", fg="white")
# click.pack(padx=30, pady=10)
# label = Label(root, text="", font="ariel 15 bold")
# label.pack(padx=30, pady=10)
# click.bind("<Button-1>", clicked)
# root.mainloop()

######################################################################


# from tkinter import *
# # create a window as root using Tk() function
# root = Tk()
# root.geometry("200x200")    
# # create a changecolor function
# # to change background color of window
# def changecolor(event):
#     # get selected list box color item
#     color=listbox.get(ANCHOR)
#     # configure color to the window
#     root.configure(bg=color)
# # create listbox 
# listbox = Listbox(root , font=('times 20 bold'), height=5,width=10)
# # insert color items into listbox
# listbox.insert(1, 'pink')
# listbox.insert(2, 'skyblue') 
# listbox.insert(3, 'green2') 
# listbox.insert(4, 'red')
# listbox.pack(pady=30)
# # bind the click event with listbox and
# # call changecolor() function
# listbox.bind('<<ListboxSelect>>', changecolor)
# root.mainloop() 


###############CMD
# import subprocess, os

# subprocess.Popen('cmd.exe')

# os.system("cmd.exe") 