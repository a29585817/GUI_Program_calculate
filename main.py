import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

mile_label = tkinter.Label(text="Miles", font=("Arial", 10, "bold"))
mile_label.grid(column=2, row=0)
# Label
eqal_label = tkinter.Label(text="is equal to ", font=("Arial", 10, "bold"))
eqal_label.grid(column=0, row=1)

calculate_label = tkinter.Label(text="0", font=("Arial", 10, "bold"))
calculate_label.grid(column=1, row=1)
calculate_label.config(padx=50)

km_label = tkinter.Label(text="Km", font=("Arial", 10, "bold"))
km_label.grid(column=2, row=1)


def button_clicked():
    calculate = round(float(input.get()) / 0.62137, 2)
    calculate_label["text"] = calculate
    calculate_label.grid(column=1, row=1)


# Botton
calculate_button = tkinter.Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

# new_button = tkinter.Button(text="New Button", command=button_clicked)
# new_button.grid(column=2, row=0)
# #Entry
input = tkinter.Entry(text="0", width=10)
input.get()
input.grid(column=1, row=0)

window.mainloop()
