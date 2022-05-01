class variables():
    # def returning_hours():
    #     for x in range(1,13):
    #         return str(x) + ","
    #hours = (1,)(2,)(3,)(4,)
    pass

#variables.returning_hours()
from tkinter import Tk, Checkbutton, IntVar, Frame, Label
from functools import partial

task_list = ['Task 1', 'Task 2', 'Task 3', 'Work', 'Study']


def choose(index, task):
    print(f'Selected task: {task}' if var_list[index].get() == 1 else f'Unselected task: {task}')


root = Tk()

Label(root, text='Tasks').grid(column=0, row=0)

frame = Frame(root)
frame.grid(column=0, row=1)

var_list = []

for index, task in enumerate(task_list):
    var_list.append(IntVar(value=0))
    Checkbutton(frame, variable=var_list[index],
                text=task, command=partial(choose, index, task)).pack()

root.mainloop()