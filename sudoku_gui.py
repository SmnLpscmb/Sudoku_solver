#Sudoku GUI

from tkinter import *
from tkinter import messagebox
from sudoku import Sudoku

root = Tk()
root.title('Sudoku Solver')
root.iconbitmap('D:/Simon/Python/Tkinter/basic_icon.ico')

top_frame = Frame(root, width=400, height=250)
top_frame.grid(row=0, sticky="EW", padx=20, pady=20)
bottom_frame = Frame(root, width=400, height=250)
bottom_frame.grid(row=1, sticky="EW", padx=20, pady=20)

title = Label(top_frame, text='Enter your Sudoku:', padx=40)
title.config(font=("Courier", 14))
title.grid(row=0, column=0, columnspan=9)

class WrongInputError(Exception):
    pass

def solve_sudoku():
    sudoku = []
    counter = 0
    try:
        for i in range(9):
            row = []
            for j in range(9):
                if len(cases[counter].get()) > 1:
                    messagebox.showerror("Error", "Wrong input in case !")
                    raise WrongInputError
                if cases[counter].get() == '':
                    row.append('0')
                else:
                    row.append(cases[counter].get())
                cases[counter].delete(0,END)
                counter += 1
            sudoku.append(row)
        user_input = Sudoku(sudoku)
        user_input.solve()
        mylabel = Label(bottom_frame, text=user_input)
        mylabel.grid(row=0, column=4, padx=100)
    except WrongInputError:
        pass

cases = []
for i in range(1,10):
    y = 1
    if (i-1) % 3 == 0:
        y = 10
    for j in range(9):
        x = 1
        if j % 3 == 0:
            x = 10
        case = Entry(top_frame, width=3, borderwidth=2, justify=CENTER)
        case.grid(row=i, column=j, padx=(2*x,0), pady=(2*y, 0))
        cases.append(case)

solve_bttn = Button(top_frame, text='Solve', padx=20, pady=20, command=solve_sudoku)
solve_bttn.grid(row=4, column=10, rowspan=3, columnspan=3, padx=(30,0))

root.mainloop()