# surface with possibilitie to create up tp 6(will maybe be extended) timer
# timer will count incremented, that is accureate enough for the use

# import
from pickle import TRUE
import tkinter as tk
from tkinter import ttk
from tkinter import *
import time

# def variables
start_time = 0
pause_time = 0
total_time = 0
timer = {}

paused = False





# root window
root = tk.Tk()
root.geometry("200x150")
root.resizable(False, False)
root.title('Work Timer')

# store initial timer
timer[0] = tk.StringVar()

# frame to name timer
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# ground timer label + entry
timer[0] = ttk.Label(signin, text="Enter name of timer: ")
timer[0].pack(fill='x', expand=True)

ground_timer_entry = ttk.Entry(signin, textvariable=ground_timer)
ground_timer_entry.pack(fill='x', expand=True)
ground_timer_entry.focus()

# start button
start_button = ttk.Button(signin, text="Start", command=start_clicked)
start_button.pack(fill='x', expand=True, pady=10)

# frame to run the timer
counting = ttk.Frame(root)
counting.pack(padx=10, pady=10, fill='x', expand=True)

root.mainloop()