# coding=utf-8
from tkinter import *
from tkinter.messagebox import *

from PIL import ImageTk, Image

font = ('Arial', 25, 'bold')

# function to clear all input

def all_clear():
    textField.delete(0, END)

#function to erase individual inputs in calculator
def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)

#function for handling click 
def click_btn_function(event):
    print("you clicked button")
    b = event.widget
    text = b['text']
    print(text)

    if text == "=":
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)

        except Exception as e:
            print("Error", e)
            showerror("Error", e)
        return

    textField.insert(END, text)


# creating a window
window = Tk()

window.title('My calculator')

# window.geometry('widthxheight')
window.geometry('800x800')

# picture label
pic = ImageTk.PhotoImage(Image.open("calc.png"))
# headingLabel=Label(window,text="my label")
headingLabel = Label(window, image=pic)
headingLabel.pack(side=TOP, pady=10)

# heading level
heading = Label(window, text='My Calculator', font=font)
heading.pack(side=TOP, pady=10)

# textfield
textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=20, fill=X, padx=10)

# buttons
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)

# adding button to frame
# row loop
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief="solid", activebackground='orange')
        btn.grid(row=i, column=j, padx=5, pady=5)
        temp += 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text="0", font=font, width=5, relief="solid")
zeroBtn.grid(row=3, column=0, padx=5, pady=5)

dotBtn = Button(buttonFrame, text=".", font=font, width=5, relief="solid")
dotBtn.grid(row=3, column=1, padx=5, pady=5)

equalBtn = Button(buttonFrame, text="=", font=font, width=5, relief="solid")
equalBtn.grid(row=3, column=2, padx=5, pady=5)

plusBtn = Button(buttonFrame, text="+", font=font, width=5, relief="solid")
plusBtn.grid(row=0, column=3, padx=5, pady=5)

minusBtn = Button(buttonFrame, text="-", font=font, width=5, relief="solid")
minusBtn.grid(row=1, column=3, padx=5, pady=5)

multiplyBtn = Button(buttonFrame, text="*", font=font, width=5, relief="solid")
multiplyBtn.grid(row=2, column=3, padx=5, pady=5)

divideBtn = Button(buttonFrame, text="/", font=font, width=5, relief="solid")
divideBtn.grid(row=3, column=3, padx=5, pady=5)

clearBtn = Button(buttonFrame, text="<--", font=font, width=13, relief="solid", command=clear)
clearBtn.grid(row=4, column=0, padx=6, pady=5, columnspan=2)

allClearBtn = Button(buttonFrame, text="AC", font=font, width=13, relief="solid", command=all_clear)
allClearBtn.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)

multiplyBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)

# btn1=Button(buttonFrame,text="1",font=font)
# btn1.grid(row=0,column=0)

# btn2=Button(buttonFrame,text="2",font=font)
# btn2.grid(row=0,column=1)


# MAIINLOoop window lai loop mma rakhidnx
# continuously visible
window.mainloop()
