import tkinter as tk

def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")
expression = ""
input_text = tk.StringVar()
input_frame = tk.Frame(window)
input_frame.pack()
input_field = tk.Entry(input_frame, textvar=input_text, font=('arial', 18, 'bold'), bd=30, insertwidth=4, width=14, justify='right')
input_field.grid(row=0, column=0)
input_field.pack()

button_frame = tk.Frame(window)
button_frame.pack()

buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', '',
    '1', '2', '3', '-', '',
    '0', '.', '=', '+', ''
]

row_value = 0
column_value = 0

for button in buttons:
    if button == '':
        column_value += 1
        continue

    action = lambda x=button: button_click(x) if x not in ['C', '='] else (button_clear() if x == 'C' else button_equal())

    tk.Button(button_frame, text=button, font=('arial', 18, 'bold'), fg='black', height=3, width=9, bd=1, command=action).grid(row=row_value, column=column_value)

    column_value += 1
    if column_value > 4:
        column_value = 0
        row_value += 1

window.mainloop()
