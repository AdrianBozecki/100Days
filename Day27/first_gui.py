import tkinter


def button_clicked():
    my_label["text"] = input.get()

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=600, height=600)
window.config(padx=100, pady=200)

#Label
my_label = tkinter.Label(text="I Am a label", font=("Arial", 24, "italic"))
my_label.config(text="Changed label")
my_label.grid(column=0, row=0, padx=20, pady=20)

#Button
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

#NewButton
new_button = tkinter.Button(text="Click me too", command=button_clicked)
new_button.grid(column=2, row=0)


#Entry
input =  tkinter.Entry()
input.grid(column=3, row=2)











window.mainloop()