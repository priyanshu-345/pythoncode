from tkinter import *
 
# globally declare the expression variable 
expression = "" 
def press(num):
    # point out the global expression variable 
    global expression 
 
    # concatenation of string 
    expression = expression + str(num) 
 
    equation.set(expression) 
 
 
def equalpress(): 
   
    try: 
        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except: 
        equation.set(" error ") 
        expression = "" 
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 

if __name__ == "__main__": 
    # create a GUI window 
    w= Tk() 
    w.configure(background="black") 
    w.title("Simple Calculator") 
    w.geometry("270x150") 
    equation = StringVar() 
    expression_field = Entry(w, textvariable=equation) 
    expression_field.grid(columnspan=4, ipadx=70)

    button1 = Button(w, text=' 1 ', fg='black', bg='orange', 
    command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 
 
    button2 = Button(w, text=' 2 ', fg='black', bg='red', 
    command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
 
    button3 = Button(w, text=' 3 ', fg='black', bg='white', 
    command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
 
    button4 = Button(w, text=' 4 ', fg='black', bg='brown', 
    command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
 
    button5 = Button(w, text=' 5 ', fg='black', bg='blue', 
    command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
 
    button6 = Button(w, text=' 6 ', fg='black', bg='cyan', 
    command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
 
    button7 = Button(w, text=' 7 ', fg='black', bg='green', 
    command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
 
    button8 = Button(w, text=' 8 ', fg='black', bg='pink', 
    command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
 
    button9 = Button(w, text=' 9 ', fg='black', bg='yellow', 
    command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
 
    button0 = Button(w, text=' 0 ', fg='black', bg='magenta', 
    command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 
 
    plus = Button(w, text=' + ', fg='black', bg='yellow', 
    command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 
 
    minus = Button(w, text=' - ', fg='black', bg='pink', 
    command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 
 
    multiply = Button(w, text=' * ', fg='black', bg='yellow', 
    command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 
 
    divide = Button(w, text=' / ', fg='black', bg='red', 
    command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 
 
    equal = Button(w, text=' = ', fg='black', bg='green', 
    command=equalpress, height=1, width=7) 
    equal.grid(row=5, column=2) 
 
    clear = Button(w, text='Clear', fg='black', bg='white', 
    command=clear, height=1, width=7) 
    clear.grid(row=5, column='1') 
 
    Decimal= Button(w, text='.', fg='black', bg='brown', 
    command=lambda: press('.'), height=1, width=7) 
    Decimal.grid(row=6, column=0) 
    # start the GUI 
    w.mainloop() 