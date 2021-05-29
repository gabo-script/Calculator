import tkinter as tk
import parser

root = tk.Tk()
root.resizable(0, 0)
root.title('Calculator')
root.config(bg='#121212')

# Logo 
photo = tk.PhotoImage(file='img/calculator.png')
root.iconphoto(False, photo)

display = tk.Entry(
    root,
    bg='#242424',
    fg='#FFFFFF',
    justify='right'
)
display.grid(row=1, columnspan=6, sticky='we')


# Funcionality
def start():

    display.insert(0, '0')


display.config(command=start())


def clearDisplay():

    display.delete(0, 'end')


i = 0  # Number index


def getNumber(num):

    global i

    if display.get() == 'Error':
        clearDisplay()
        display.insert(i, num)
        i += 1

    elif display.get() == '0':
        clearDisplay()
        display.insert(i, num)
        i += 1

    else:
        display.insert(i, num)
        i += 1


def getOperation(operator):

    global i

    operator_length = len(operator)
    display.insert(i, operator)
    i += operator_length


def undo():

    display_status = display.get()

    if len(display_status):

        new_display = display_status[:-1]
        clearDisplay()
        display.insert(0, new_display)

    else:
        clearDisplay()
        display.insert(0, 'Error')


def equal():

    display_status = display.get()

    try:
        math = parser.expr(display_status).compile()
        result = eval(math)
        clearDisplay()
        display.insert(0, result)

    except SyntaxError:
        clearDisplay()
        display.insert(0, 'Error')


# Numeric buttons
tk.Button(
    root,
    text='1',
    command=lambda: getNumber(1),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=2, column=0, sticky='we')

tk.Button(
    root,
    text='2',
    command=lambda: getNumber(2),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=2, column=1, sticky='we')

tk.Button(
    root,
    text='3',
    command=lambda: getNumber(3),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=2, column=2, sticky='we')


tk.Button(
    root,
    text='4',
    command=lambda: getNumber(4),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=3, column=0, sticky='we')

tk.Button(
    root,
    text='5',
    command=lambda: getNumber(5),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=3, column=1, sticky='we')

tk.Button(
    root,
    text='6',
    command=lambda: getNumber(6),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=3, column=2, sticky='we')


tk.Button(
    root,
    text='7',
    command=lambda: getNumber(7),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=4, column=0, sticky='we')

tk.Button(
    root,
    text='8',
    command=lambda: getNumber(8),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=4, column=1, sticky='we')

tk.Button(
    root,
    text='9',
    command=lambda: getNumber(9),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=4, column=2, sticky='we')

# Operation buttons
tk.Button(
    root,
    text='C',
    command=lambda: clearDisplay(),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=5, column=0, sticky='we')

tk.Button(
    root,
    text='0',
    command=lambda: getNumber(0),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=5, column=1, sticky='we')

tk.Button(
    root,
    text='.',
    command=lambda: getOperation('.'),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=5, column=2, sticky='we')


tk.Button(
    root,
    text='+',
    command=lambda: getOperation(' + '),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=2, column=3, sticky='we')

tk.Button(
    root,
    text='-',
    command=lambda: getOperation(' - '),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=3, column=3, sticky='we')

tk.Button(
    root,
    text='x',
    command=lambda: getOperation(' * '),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=4, column=3, sticky='we')

tk.Button(
    root,
    text='/',
    command=lambda: getOperation(' / '),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=5, column=3, sticky='we')


tk.Button(
    root,
    text='⌫',
    command=lambda: undo(),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=2, column=4, columnspan=2, sticky='we')

tk.Button(
    root,
    text='exp',
    command=lambda: getOperation('**'),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=3, column=4, sticky='we')

tk.Button(
    root,
    text='^2',
    command=lambda: getOperation('**2'),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=3, column=5, sticky='we')

tk.Button(
    root,
    text='(',
    command=lambda: getOperation('('),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=4, column=4, sticky='we')

tk.Button(
    root,
    text=')',
    command=lambda: getOperation(')'),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=4, column=5, sticky='we')

tk.Button(
    root,
    text='=',
    command=lambda: equal(),
    bg='#242424',
    fg='#FFFFFF'
).grid(row=5, column=4, columnspan=2, sticky='we')

root.mainloop()
