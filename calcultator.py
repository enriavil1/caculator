from tkinter import *

root = Tk()

root.title("Calculator")

input_box = Entry(root, width = 50, borderwidth = 5)
input_box.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def click(num):
    box = input_box.get()
    box += str(num)
    input_box.delete(0, END)
    input_box.insert(0, box)

def clear():
    input_box.delete(0, END)

def add():
    variable = input_box.get()
    global first_num
    first_num = int(variable)
    global math
    math = "add"
    input_box.delete(0, END)

def substract():
    variable = input_box.get()
    global first_num
    first_num = int(variable)
    global math
    math = "substract"
    input_box.delete(0, END)

def divide():
    variable = input_box.get()
    global first_num
    first_num = int(variable)
    global math
    math = "divide"
    input_box.delete(0, END)

def multiply():
    variable = input_box.get()
    global first_num
    first_num = int(variable)
    global math
    math = "multiply"
    input_box.delete(0, END)

def equal():
    if math == "add":
        second_number = input_box.get()
        input_box.delete(0,END)
        result = first_num + int(second_number)
        input_box.insert(0, str(result))

    if math == "substract":
        second_number = input_box.get()
        input_box.delete(0,END)
        result = first_num - int(second_number)
        input_box.insert(0, str(result))

    if math == "multiply":
        second_number = input_box.get()
        input_box.delete(0,END)
        result = first_num * int(second_number)
        input_box.insert(0, str(result))

    if math == "divide":
        second_number = input_box.get()
        input_box.delete(0,END)
        result = first_num / int(second_number)
        input_box.insert(0, str(result))


#Buttons created

num_1 = Button(root, text= "1", padx = 90, pady = 30, command = lambda:click(1) )
num_2 = Button(root, text= "2", padx = 90, pady = 30, command = lambda:click(2) ) 
num_3 = Button(root, text= "3", padx = 90, pady = 30, command = lambda:click(3) )

num_4 = Button(root, text= "4", padx = 90, pady = 30, command = lambda:click(4) )
num_5 = Button(root, text= "5", padx = 90, pady = 30, command = lambda:click(5) )
num_6 = Button(root, text= "6", padx = 90, pady = 30, command = lambda:click(6) )

num_7 = Button(root, text= "7", padx = 90, pady = 30, command = lambda:click(7) )
num_8 = Button(root, text= "8", padx = 90, pady = 30, command = lambda:click(8) )
num_9 = Button(root, text= "9", padx = 90, pady = 30, command = lambda:click(9) )

num_0 = Button(root, text= "0", padx = 90, pady = 30, command = lambda:click(0) )
button_clear = Button(root, text= "clear", padx = 80, pady = 30, command = clear)
button_equal = Button(root, text= "=", padx = 90, pady = 30, command = equal)

button_minus= Button(root, text= "-", padx = 90, pady = 30, command = substract)
button_plus = Button(root, text= "+", padx = 90, pady = 30, command = add )
button_times = Button(root, text= "*", padx = 90, pady = 30, command = multiply )
button_divide = Button(root, text= "/", padx = 90, pady = 30, command = divide )


#Button inserting
num_0.grid(row = 4, column = 0)
button_clear.grid(row = 4, column = 1, columnspan = 1)
button_equal.grid(row = 4, column = 2)
button_divide.grid(row = 4, column = 3)

num_1.grid(row = 3, column = 0)
num_2.grid(row = 3, column = 1)
num_3.grid(row = 3, column = 2)
button_times.grid(row = 3, column = 3)

num_4.grid(row = 2, column = 0)
num_5.grid(row = 2, column = 1)
num_6.grid(row = 2, column = 2)
button_minus.grid(row = 2, column = 3)

num_7.grid(row = 1, column = 0)
num_8.grid(row = 1, column = 1)
num_9.grid(row = 1, column = 2)
button_plus.grid(row = 1, column = 3)


root.mainloop()








