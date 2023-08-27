import tkinter as tk

def show_output():
    number = int(numbers_input.get())

    if number == 0:
        output_label.configure(text='get off')
        return

    output = ''
    for i in range(1, 13):
        output += str(number) + 'x' + str(i)
        output += ' = '+str(number * i) + '\n'

    output_label.configure(text=output)

window = tk.Tk()
window.title('JustPython')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='สูตรคูณ', fg="blue")
title_label.pack(pady=20)


numbers_input = tk.Entry(master=window, width=15)
numbers_input.pack(pady=20)

go_button = tk.Button(
    master=window, text='ได้แก่',
    command=show_output, width=15, height=2

)
go_button.pack()

output_label = tk.Label(master=window)
output_label.pack()

window.mainloop()