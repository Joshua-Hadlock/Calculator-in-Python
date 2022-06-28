#Joshua Hadlock
#A1
#computer programming 2
#I did not cheat


#This is a calculator!!!


#get the tk code
import tkinter as tk

#create the window to display stuff
window = tk.Tk()
window.title("calculator")
window.geometry("230x155")


#variables
variable1 = ""
variable2 = ""
operater = False
operation = ''
equation = ''
#functions when you click buttons

#any number button
def btn1(button):
	global variable1
	global variable2
	global equation
	global counter
	output.delete(0,100)
	if operater == False:
		variable1 = variable1 + button
		output.insert(tk.END,variable1)
		equation += button
	else:
		variable2 = variable2 + button
		output.insert(tk.END,variable2)
		equation += button

#operator button
def operate(button):
	global operation
	global operater
	global equation
	global variable2
	operation = ''
	equation += button
	operater = True
	output.delete(0,100)
	output.insert(tk.END,button)
	variable2 = ''


#button for when you click the = button
def equal_equation():
	global equation
	global operation
	global variable1
	global variable2
	global operater
	output.delete(0,100)
	answer = eval(equation)
	output.insert(tk.END,answer)
	variable1 = ""
	variable2 = ""
	operater = False
	operation = ''
	equation = ''

#button that clears the screen and resets everything
def clear_screen():
	global equation
	global operation
	global variable1
	global variable2
	global operater
	output.delete(0,100)
	variable1 = ""
	variable2 = ""
	operater = False
	operation = ''
	equation = ''

#create the grid system for the calculator to easily fall in place
hello = tk.Label()
hello.grid(row=5, column=4)

#create the output button that's larger than the rest of the buttons
output = tk.Entry(width=12)
output.grid(columnspan=2, row=1, column=1)


#rest of the calculator buttons
number1 = tk.Button(text="1", command = lambda b='1':btn1(b))
number1.config(height=1, width=3)
number1.grid(row=4,column=1)

number2 = tk.Button(text="2", command = lambda b='2':btn1(b))
number2.config(height=1, width=3)
number2.grid(row=4,column=2)

number3 = tk.Button(text="3", command = lambda b='3':btn1(b))
number3.config(height=1, width=3)
number3.grid(row=4,column=3)

number4 = tk.Button(text="4", command = lambda b='4':btn1(b))
number4.config(height=1, width=3)
number4.grid(row=3,column=1)

number5 = tk.Button(text="5", command = lambda b='5':btn1(b))
number5.config(height=1, width=3)
number5.grid(row=3,column=2)

number6 = tk.Button(text="6", command = lambda b='6':btn1(b))
number6.config(height=1, width=3)
number6.grid(row=3,column=3)

number7 = tk.Button(text="7", command = lambda b='7':btn1(b))
number7.config(height=1, width=3)
number7.grid(row=2,column=1)

number8 = tk.Button(text="8", command = lambda b='8':btn1(b))
number8.config(height=1, width=3)
number8.grid(row=2,column=2)

number9 = tk.Button(text="9", command = lambda b='9':btn1(b))
number9.config(height=1, width=3)
number9.grid(row=2,column=3)


#create the zero button slightly larger than the rest
number0 = tk.Button(text="0", command = lambda b='0':btn1(b))
number0.config(height=1, width=10)
number0.grid(columnspan=2,row=5,column=1)


#back to normal buttons
slash = tk.Button(text="/", command = lambda b='/':operate(b))
slash.config(height=1, width=3)
slash.grid(row=1,column=4)

star = tk.Button(text="*", command = lambda b='*':operate(b))
star.config(height=1, width=3)
star.grid(row=2,column=4)

minus = tk.Button(text="-", command = lambda b='-':operate(b))
minus.config(height=1, width=3)
minus.grid(row=3,column=4)

plus = tk.Button(text="+", command = lambda b='+':operate(b))
plus.config(height=1, width=3)
plus.grid(row=4,column=4)

equal = tk.Button(text="=", command = equal_equation)
equal.config(height=1, width=3)
equal.grid(row=5,column=4)

dot = tk.Button(text=".", command = lambda b='.':btn1(b))
dot.config(height=1, width=3)
dot.grid(row=5,column=3)

clear = tk.Button(text="clr", command = clear_screen)
clear.config(height=1, width=3)
clear.grid(row=1,column=3)
tk.mainloop()