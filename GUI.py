import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import Logic
import functools
from threading import Thread

entry_list = []
entry_variable_list = []

def Create_Thread(func):
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs):
        new_thread = Thread(target=func, args=func_args, kwargs=func_kwargs, daemon=True)
        new_thread.start()
    return wrapper

@Create_Thread
def Clear():
    for y in range(9):
        for x in range(9):
            entry_variable_list[y][x].set('')

    entry_list[0][0].update_idletasks()

@Create_Thread
def Solve():
    grid = []

    for y in range(9):
        temp = []
        for x in range(9):
            number = entry_list[y][x].get()
            if number == '':
                msg.showerror('', 'There is a missing entry.\nPlease enter a number for that entry.')
                entry_list[y][x].focus()
                return
            else:
                number = int(entry_list[y][x].get())
                temp.append(number)
        grid.append(temp)

    _, grid = Logic.solve(grid)
    
    check = True
    for y in range(9):
        if check == True:
            for x in range(9):
                if grid[y][x] == 0:
                    check = False
                    break
        else:
            break

    if check == True:
        for y in range(9):
            for x in range(9):
                entry_variable_list[y][x].set(str(grid[y][x]))
        entry_list[0][0].update_idletasks()
    else:
        msg.showerror('', "The puzzle you have entered has no solution.\nPlease check whether you have entered the numbers correctly.")
    
def Validate_Entry(data):
    if data == '':
        return True
    elif len(data) == 1 and data.isnumeric():
        return True
    elif not data.isnumeric():
        msg.showerror('', f"You have entered '{data}'.\nError: Only numbers are allowed.")
        return False
    elif len(data) != 1:
        msg.showerror('', f"You have entered '{data}'.\nError: Only numbers less than 10 are allowed.")
        return False
    else:
        return False

def Setup_Entrys(puzzle_frame):
    global entry_list, entry_variable_list

    reg = puzzle_frame.register(Validate_Entry)
    
    for y in range(9):
        temp = []
        for x in range(9):
            strVar = tk.StringVar()
            strVar.set('')
            temp.append(strVar)
        entry_variable_list.append(temp)
    
    for y in range(9):
        temp = []
        for x in range(9):
            temp.append(ttk.Entry(puzzle_frame, textvariable=entry_variable_list[y][x], width=3, justify=tk.CENTER, font=('Arial', '20'), validatecommand=(reg, '%P'), validate='key'))
        entry_list.append(temp)

def Main_Setup():
    global entry_list
    
    window = tk.Tk()
    window.title('Sudoku Solver')

    label_frame = tk.Frame(window, height=150, width=800, bd=3)
    label_frame.grid(row=0, columnspan=2, sticky='W')
    
    label0 = ttk.Label(label_frame, text='Instructions', font=('Arial', '20'))
    label0.grid(row=0, columnspan=2, sticky='W')
    
    ttk.Label(label_frame, text='1.', font=('Arial', '16')).grid(column=0, row=1, sticky='W')
    ttk.Label(label_frame, text='This program will solve your Sudoku puzzle.', font=('Arial', '16')).grid(column=1, row=1, sticky='W')
    ttk.Label(label_frame, text='2.', font=('Arial', '16')).grid(column=0, row=2, sticky='W')
    ttk.Label(label_frame, text='Enter the numbers of your puzzle below.', font=('Arial', '16')).grid(column=1, row=2, sticky='W')
    ttk.Label(label_frame, text='3.', font=('Arial', '16')).grid(column=0, row=3, sticky='W')
    ttk.Label(label_frame, text='Enter 0 for blanks.', font=('Arial', '16')).grid(column=1, row=3, sticky='W')
    ttk.Label(label_frame, text='4.', font=('Arial', '16')).grid(column=0, row=4, sticky='W')
    ttk.Label(label_frame, text="Click the 'Solve puzzle' button to get the solution.", font=('Arial', '16')).grid(column=1, row=4, sticky='W')
    ttk.Label(label_frame, text='5.', font=('Arial', '16')).grid(column=0, row=5, sticky='W')
    ttk.Label(label_frame, text="Click the 'Clear puzzle' button to clear your entries.", font=('Arial', '16')).grid(column=1, row=5, sticky='W')
    
    puzzle_frame = tk.Frame(window, height=500, width=500)
    puzzle_frame.grid(column=0, row=1, sticky='NW')
    
    Setup_Entrys(puzzle_frame)
    for y in range(9):
        for x in range(9):
            entry_list[y][x].grid(column=x, row=y, sticky='W')

    button_frame = tk.Frame(window, height=500, width=300)
    button_frame.grid(column=1, row=1)
    
    solve_button = tk.Button(button_frame, text='Solve puzzle', font=('Arial', '16'), command=Solve, padx=3, pady=3)
    solve_button.grid(row=0)
    clear_button = tk.Button(button_frame, text='Clear puzzle', font=('Arial', '16'), command=Clear, padx=3, pady=3)
    clear_button.grid(row=1)
    quit_button = tk.Button(button_frame, text='Quit program', font=('Arial', '16'), command=window.destroy, padx=3, pady=3)
    quit_button.grid(row=2)
    
    window.mainloop()

Main_Setup()
