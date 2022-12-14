from tkinter import *

# Entry from buttons mechanism
# -----------------------
# I take the ammount of characters that were entered into the entry and put the number in one position ahead the last one.
def write_number(number):
    last_index = len(entry.get())+1
    entry.insert(last_index, number)
# -----------------------
# Operations:
# ----------------------------------
def operation(sign):
    if entry.get() != '':
        if sign in ['+','-','/','*']:
            global operation_sign
            operation_sign = sign
            global number1
            number1 = int(entry.get())
            entry.delete(0, END)
        elif sign == '=':
            global number2
            number2 = int(entry.get())
            entry.delete(0, END)
            result = eval(f'{number1}{operation_sign}{number2}')
            entry.insert(0, str(result))
# -----------------------------------
# Clean entry:
#------------------------------------
def clean_entry():
    global number1
    number1 = 0
    number2 = 0
    entry.delete(0, END)
#------------------------------------

window = Tk()
window.title('Calculator')
window.geometry('400x334')
window.resizable(0, 0)

# ROW 0
entry = Entry(window, bg='#605B5B', font=('Helvetiva', 27))
entry.grid(row=0, column=0, columnspan=4)

# ROW 1
one = Button(window, text=1, font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: write_number(1))
one.grid(row=1, column=0, sticky='nesw')

two = Button(window, text=2, font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: write_number(2))
two.grid(row=1, column=1,sticky='nesw')

three = Button(window, text=3, font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: write_number(3))
three.grid(row=1, column=2, sticky='nesw')

plus = Button(window, text='+', font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: operation('+'))
plus.grid(row=1, column=3, sticky='nesw')

# ROW 2
four = Button(window, text=4, font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: write_number(4))
four.grid(row=2, column=0, sticky='nesw')

five = Button(window, text=5, font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: write_number(5))
five.grid(row=2, column=1,sticky='nesw')

six = Button(window, text=6, font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: write_number(6))
six.grid(row=2, column=2, sticky='nesw')

minus = Button(window, text='-', font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: operation('-'))
minus.grid(row=2, column=3, sticky='nesw')

# ROW 3
seven = Button(window, text=7, font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: write_number(7))
seven.grid(row=3, column=0, sticky='nesw')

eight = Button(window, text=8, font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: write_number(8))
eight.grid(row=3, column=1,sticky='nesw')

nine = Button(window, text=9, font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: write_number(9))
nine.grid(row=3, column=2, sticky='nesw')

multiply = Button(window, text='*', font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: operation('*'))
multiply.grid(row=3, column=3, sticky='nesw')

# ROW 4
space1 = Button(window, text='C', font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: clean_entry())
space1.grid(row=4, column=0, sticky='nesw')

zero = Button(window, text=0, font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: write_number(0))
zero.grid(row=4, column=1,sticky='nesw')

equal = Button(window, text='=', font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: operation('='))
equal.grid(row=4, column=2, sticky='nesw')

divide = Button(window, text='/', font=('Helvetiva', 27), fg='#FFFFFF', bg='#000000', command=lambda: operation('/'))
divide.grid(row=4, column=3, sticky='nesw')

window.mainloop()