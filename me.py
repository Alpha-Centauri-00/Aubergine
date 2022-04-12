
import glob
import tkinter as tk
from tkinter import Tk, ttk
from tkinter.messagebox import showinfo
from turtle import onclick
#from numpy import var
#from click import command
#from setuptools import Command


class The_App():
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title('Run Robot Test Cases')
        self.root.geometry('620x200')
        self.columns = ('first_name')   # define columns
        self.tree = ttk.Treeview(self.root, columns=self.columns, show='headings')
        self.tree.heading('first_name', text='Test Cases')  # define headings
        # tree.heading('last_name', text='Last Name')
        # tree.heading('email', text='Email')


        # generate sample data
        files = glob.glob("*.robot")
        contacts = []
        for n in files:
            contacts.append((f'{n}'))

        # add data to the treeview
        for contact in contacts:
            self.tree.insert('', tk.END, values=contact)



        def item_selected_(event):
            for item in self.tree.selection():
                    item_text = self.tree.item(item)
                    text_is = item_text['values']
                    my_label.config(text="robot "+ text_is[0])
            

        my_label = ttk.Label(self.root,text="")
        my_label.place(x=400, y=20)
        self.tree.bind('<<TreeviewSelect>>', item_selected_)



        self.tree.grid(row=0, column=0, sticky='nsew')
        btn = tk.Button(self.root, text = 'Run!', bd = '1',command = self.root.destroy)
        btn.place(x=625, y=20)

# add a scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.root.mainloop()



if __name__ == "__main__":
    app = The_App()
