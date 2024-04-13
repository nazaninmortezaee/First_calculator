import tkinter
from tkinter import *
import tkinter

# Creating the GUI window.
window = tkinter.Tk()
window.title("Calculator")
window.geometry("380x440")
window.resizable(0,0)
window.config(bg = "gray13")


# Creating our text widget.
sample_text = tkinter.Entry(window,width=13, font=("arial", 35),fg="white", bg= "gray3")
sample_text.pack()

# Creating the function to set the text
# with the help of button

def set_text_1():
	sample_text.insert("end", "1")

def set_text_2():
	sample_text.insert("end", "2")

def set_text_3():
	sample_text.insert("end", "3")


def set_text_4():
	sample_text.insert("end", "4")

def set_text_5():
	sample_text.insert("end", "5")

def set_text_6():
	sample_text.insert("end", "6")

def set_text_7():
	sample_text.insert("end", "7")

def set_text_8():
	sample_text.insert("end", "8")

def set_text_9():
	sample_text.insert("end", "9")

def set_text_plus():
	sample_text.insert("end", "+")

def minus():
    sample_text.insert("end", "-")

def devide():
    sample_text.insert("end", "/")

def set_text_dot():
    sample_text.insert("end", ".")

def set_text_zero():
    sample_text.insert("end", "0")

def multiply():
    sample_text.insert("end", "*")

def reset():
	sample_text.delete(0, "end")


def delete():
    text = sample_text.get()
    sample_text.delete(0, "end")
    sample_text.insert(0, text[:-1])

def result():
    res = eval(sample_text.get())
    sample_text.delete(0, "end")
    sample_text.insert(0, res)


btn1 = tkinter.Button(window,text= "1", width=4, height=1, font= ("arial", 20, "bold"), bd= 1, fg="white", bg="gray35", command=set_text_1).place(x=20, y=285)


btn2 = tkinter.Button(window,text="2", width=4, height=1, font= ("arial", 20, "bold"), bd= 1, fg="white", bg="gray35", command=set_text_2).place(x=107, y=285)


btn3 = tkinter.Button(window, text="3", width=4, height=1, font= ("arial", 20, "bold"), bd=1, fg="white", bg="gray35", command=set_text_3).place(x=193, y=285)


btn4 = tkinter.Button(window,text= "4", width=4, height=1, font= ("arial", 20, "bold"), bd= 1, fg="white", bg="gray35", command=set_text_4).place(x=20, y=220)


btn5 = tkinter.Button(window,text="5", width=4, height=1, font= ("arial", 20, "bold"), bd= 1, fg="white", bg="gray35", command=set_text_5).place(x=107, y=220)


btn6 = tkinter.Button(window, text="6", width=4, height=1, font= ("arial", 20, "bold"), bd=1, fg="white", bg="gray35", command=set_text_6).place(x=193, y=220)


btn7 = tkinter.Button(window,text= "7", width=4, height=1, font= ("arial", 20, "bold"), bd= 1, fg="white", bg="gray35", command=set_text_7).place(x=20, y=155)


btn8 = tkinter.Button(window,text="8", width=4, height=1, font= ("arial", 20, "bold"), bd= 1, fg="white", bg="gray35", command=set_text_8).place(x=107, y=155)


btn9 = tkinter.Button(window, text="9", width=4, height=1, font= ("arial", 20, "bold"), bd=1, fg="white", bg="gray35", command=set_text_9).place(x=193, y=155)


btn_dot = tkinter.Button(window, text=".", width=4, height=1, font= ("arial", 20, "bold"), bd=1, fg="white", bg="gray35", command=set_text_dot).place(x=193, y=350)


btn_zero = tkinter.Button(window, text="0", width=9, height=1, font= ("arial", 20, "bold"), bd=1, fg="white", bg="gray35", command=set_text_zero).place(x=20, y=350)





plus = tkinter.Button(window, width=4, height=1,font= ("arial", 20, "bold"), bd=1, fg="gray5", bg="gray98", text="+", command=set_text_plus).place(x=280, y=220)


result = tkinter.Button(window,text= "=", width=4, height=3, font= ("arial", 20, "bold"), bd= 1, fg="gray5", bg="gray98", command=result).place(x=280, y=285)

btn_minus = tkinter.Button(window,text= "-", width=4, height=1, font= ("arial", 20, "bold"), bd= 1, fg="gray5", bg="gray98", command=minus).place(x=280, y=155)

btn_devide = tkinter.Button(window,text= "/", width=4, height=1, font= ("arial", 20, "bold"), bd= 1, fg="white", bg="darkorange", command=devide).place(x=280, y=90)

btn_multiply = tkinter.Button(window,text= "*", width=4, height=1, font= ("arial", 20, "bold"), bd= 1, fg="white", bg="darkorange", command=devide).place(x=193, y=90)

reset = tkinter.Button(window,  text="C",width=4, height=1 ,font= ("arial", 20, "bold"), bd= 1, fg="white", bg="darkorange",command=reset).place(x=20, y=90)


delete = tkinter.Button(window, text="D",width=4, height=1 ,font= ("arial", 20, "bold"), bd= 1, fg="white", bg="darkorange" , command=delete).place(x=107, y=90)


window.mainloop()