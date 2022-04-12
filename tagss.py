# """A directory browser using Ttk Treeview.

# Based on the demo found in Tk 8.5 library/demos/browse
# """
# import os
# import glob
# import tkinter as tk
# from tkinter import ttk
# # import Tkinter
# # import ttk

# def populate_tree(tree, node):
#     if tree.set(node, "type") != 'directory':
#         return

#     path = tree.set(node, "fullpath")
#     tree.delete(*tree.get_children(node))

#     parent = tree.parent(node)
#     special_dirs = [] if parent else glob.glob('*.robot')   # + glob.glob('..')

#     for p in special_dirs + os.listdir(path):
#         ptype = None
#         p = os.path.join(path, p).replace('\\', '/')
#         if os.path.isdir(p): ptype = "directory"
#         elif os.path.isfile(p): ptype = "file"

#         fname = os.path.split(p)[1]
#         id = tree.insert(node, "end", text=fname, values=[p, ptype])

#         if ptype == 'directory':
#             if fname not in ('.', '..'):
#                 tree.insert(id, 0, text="dummy")
#                 tree.item(id, text=fname)
#         elif ptype == 'file':
#             size = os.stat(p).st_size
#             tree.set(id, "size", "%d bytes" % size)


# def populate_roots(tree):
#     dir = os.path.abspath('.').replace('\\', '/')
#     node = tree.insert('', 'end', text=dir, values=[dir, "directory"])
#     populate_tree(tree, node)

# def update_tree(event):
#     tree = event.widget
#     populate_tree(tree, tree.focus())

# def change_dir(event):
#     tree = event.widget
#     node = tree.focus()
#     if tree.parent(node):
#         path = os.path.abspath(tree.set(node, "fullpath"))
#         if os.path.isdir(path):
#             os.chdir(path)
#             tree.delete(tree.get_children(''))
#             populate_roots(tree)

# def autoscroll(sbar, first, last):
#     """Hide and show scrollbar as needed."""
#     first, last = float(first), float(last)
#     if first <= 0 and last >= 1:
#         sbar.grid_remove()
#     else:
#         sbar.grid()
#     sbar.set(first, last)

# root = tk.Tk()

# vsb = ttk.Scrollbar(orient="vertical")
# hsb = ttk.Scrollbar(orient="horizontal")

# tree = ttk.Treeview(columns=("fullpath", "type", "size"),
#     displaycolumns="size", yscrollcommand=lambda f, l: autoscroll(vsb, f, l),
#     xscrollcommand=lambda f, l:autoscroll(hsb, f, l))

# vsb['command'] = tree.yview
# hsb['command'] = tree.xview

# tree.heading("#0", text="Directory Structure", anchor='w')
# tree.heading("size", text="File Size", anchor='w')
# tree.column("size", stretch=0, width=100)

# populate_roots(tree)
# tree.bind('<<TreeviewOpen>>', update_tree)
# tree.bind('<Double-Button-1>', change_dir)

# # Arrange the tree and its scrollbars in the toplevel
# tree.grid(column=0, row=0, sticky='nswe')
# vsb.grid(column=1, row=0, sticky='ns')
# hsb.grid(column=0, row=1, sticky='ew')
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)

# root.mainloop()

New_tags_list = []



def split_TAGS(input):
    words = input.split()
    for i in words:
        New_tags_list.append(i)
        #New_tags = list(dict.fromkeys(New_tags_list))
    print(New_tags_list[-1])
        


with open("01_robot-file.robot","r") as f:
    lines = f.readlines()
    res = []

    for line in lines:
        if "[Tags]" in line:
            #split_TAGS(line)
            word = line.split()
            word = list(dict.fromkeys(word))
            #print(word[0])
            #print("======")
            for i in word:
                if i not in res:
                    res.append(i)
                    result = i.split()
                    print(result)
            
            #print(New_tags_list[-1])
            
            #print(type(New_Tags))

# for x in lines:
#     if "[TAGS]" in lines:
#         print(x)
#     else:
#         print("no Tags found")
#from robot.parsing.model import TestData
#suite = TestData(parent=None, source=path_to_test_suite)
#for testcase in suite.testcase_table:
#    print(testcase.name)



#parsing Tags

# from robot.parsing import TestData
# import sys

# def main(path):
#     suite = TestData(parent=None, source=path)
#     tags = get_tags(suite)
#     print ", ".join(sorted(set(tags)))

# def get_tags(suite):
#     tags = []

#     if suite.setting_table.force_tags:
#         tags.extend(suite.setting_table.force_tags.value)

#     if suite.setting_table.default_tags:
#         tags.extend(suite.setting_table.default_tags.value)

#     for testcase in suite.testcase_table.tests:
#         if testcase.tags:
#             tags.extend(testcase.tags.value)

#     for child_suite in suite.children:
#         tags.extend(get_tags(child_suite))

#     return tags

# if __name__ == "__main__":
#     main(sys.argv[1])