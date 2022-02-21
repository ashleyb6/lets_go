from tkinter import *
from tkinter import messagebox, font
import random


# ---------- Generate Random Activity ------------
def generate_random():
    activity_label = Label(text="Go do this...", font="Modern 20 normal", bg='#b9fbc0')
    activity_label.grid(column=1, row=3, columnspan=2, pady=30)


# ---------- Generate Random Activity based on specification ------------
def generate_specified():
    pass


# ---------- Add an activity to CSV file ------------
def add_activity():
    pass


# ---------- Delete an activity from CSV file ------------
def delete_activity():
    pass


# ---------- Update list of activities by adding or deleting ------------
def update():
    update_window = Tk()
    update_window.title("Update Activities")
    update_window.config(pady=50, padx=50)



# ---------- UI ------------
window = Tk()
window.config(padx=50, pady=50, bg="#b9fbc0")
window.title("Let'sGo")

canvas = Canvas(window, width=200, height=200)
canvas.config(bg='#b9fbc0', highlightthickness=0, borderwidth=0)
canvas.create_oval(0, 0, 200, 200, fill='#fbf8cc', outline="")
canvas.create_text(100, 100, fill='#fe6d73', font="Modern 40 bold", text="Let'sGo")
canvas.grid(column=1, row=0, columnspan=2, pady=20, padx=20)

pick_random = Button(text="Pick Random Activity", font='Courier 12 normal', bg='#e9edc9', command=generate_random)
pick_random.grid(column=1, row=1, padx=10, pady=20)

make_specs = Button(text="Make Specifications", font='Courier 12 normal', bg='#e9edc9', command=generate_specified)
make_specs.grid(column=2, row=1, padx=10, pady=10)

update_list = Button(text="Update List of Activities", font='Courier 12 normal', bg='#e9edc9', command=update)
update_list.grid(column=1, row=2, columnspan=2, padx=10)



print(font.families())

window.mainloop()


