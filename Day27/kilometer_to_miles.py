from tkinter import *

window = Tk()
window.title("Km to Mile Converter")
window.minsize(width=230, height=120)
window.config(pady=20)


def km_to_miles():
    kilometers = float(input.get())
    miles = kilometers / 1.609
    result_label.config(text=round(miles))


# Entry
input = Entry()
input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=km_to_miles)
button.grid(column=1, row=2)

# Text1
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Text2
result_label = Label(text="0")
result_label.grid(column=1, row=1)

kilometers_label = Label(text="Km")
kilometers_label.grid(column=2, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

window.mainloop()
