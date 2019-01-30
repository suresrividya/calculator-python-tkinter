from tkinter import *
'''
global expression
expression = ""
'''
def pressed(key):
    '''
    global expression,label_text
    expression = label_text.get()+key
    cal_box.insert(INSERT,expression)
    '''
    expression = cal_box.get('1.0',END).strip()
    exp_up = result.get('1.0',END).strip()
    if expression=='0':
        expression = key
    else:
        if((key in ['/','+','-','*']) and (expression[-1] in ['/','+','-','*'])):
            expression = expression[:-1]
        expression = expression+key
       
       
    result.delete('1.0',END)
    result.insert(INSERT,expression)
        
           
    cal_box.delete('1.0',END)
    cal_box.insert(INSERT,expression)
   
def backspace():
    expression = cal_box.get('1.0',END)
    new  = expression.strip()[:-1]
    print("expression",new)
    cal_box.delete('1.0',END)
    cal_box.insert(INSERT,new)

def handleEvent(event):
    global label_text
    cal_box.delete('1.0',END)
    label_text.set("")

def equal():
    expression = cal_box.get('1.0',END)
    print("expression",expression)
    try:
        expression = eval(expression)
    except:
        expression = "Invalid Inputs"
    '''cal_box.delete('1.0',END)
    cal_box.insert(INSERT,expression)
    '''
    result.delete('1.0',END)
    result.insert(INSERT,expression)

def clear():
    #expression = cal_box.get('1.0',END)
    cal_box.delete('1.0',END)
    cal_box.insert(INSERT,'0')
    result.delete('1.0',END)

window = Tk()
window.title("Calculator")
window.geometry("200x200")

global label_text
label_text = StringVar()
label_text.set("0")


result = Text(window,width=140,height=1)
result.grid(row=0,columnspan=15)

cal_box = Text(window,width=140,height=3,font=("Arial Bold",11),fg="green")
cal_box.insert(INSERT,label_text.get())
cal_box.grid(row=1,columnspan=15)
cal_box.bind("<FocusIn>",handleEvent)

percentage = Button(window,text="%",padx=100,pady=15)
percentage.grid(row=2,column=0,pady=10)

ce = Button(window,text="CE",padx=100,pady=15)
ce.grid(row=2,column=1,pady=10)

c = Button(window,text="C",padx=100,pady=15,command=lambda: clear())
c.grid(row=2,column=2,pady=10)

back = Button(window,text="<--",padx=100,pady=15,command=lambda : backspace())
back.grid(row=2,column=3,pady=10)

divide = Button(window,text="/",padx=100,pady=15,command=lambda: pressed('/'))
divide.grid(row=2,column=4,pady=10)

sqroot = Button(window,text="Sqroot",padx=100,pady=15,command=lambda:pressed('**1/2'))
sqroot.grid(row=3,column=0,pady=10)

seven = Button(window,text="7",padx=100,pady=15,command=lambda: pressed('7'))
seven.grid(row=3,column=1,pady=10)

eight = Button(window,text="8",padx=100,pady=15,command=lambda: pressed('8'))
eight.grid(row=3,column=2,pady=10)

nine = Button(window,text="9",padx=100,pady=15,command=lambda: pressed('9'))
nine.grid(row=3,column=3,pady=10)

mul = Button(window,text="X",padx=100,pady=15,command=lambda: pressed('*'))
mul.grid(row=3,column=4,pady=10)

square = Button(window,text="x^2",padx=100,pady=15,command=lambda:pressed('**2'))
square.grid(row=4,column=0,pady=10)

four = Button(window,text="4",padx=100,pady=15,command=lambda: pressed('4'))
four.grid(row=4,column=1,pady=10)

five = Button(window,text="5",padx=100,pady=15,command=lambda: pressed('5'))
five.grid(row=4,column=2,pady=10)

six = Button(window,text="6",padx=100,pady=15,command=lambda: pressed('6'))
six.grid(row=4,column=3,pady=10)

minus = Button(window,text="-",padx=100,pady=15,command=lambda: pressed('-'))
minus.grid(row=4,column=4,pady=10)

cube = Button(window,text="x^3",padx=100,pady=15,command=lambda:pressed('**3'))
cube.grid(row=5,column=0,pady=10)

one = Button(window,text="1",padx=100,pady=15,command=lambda: pressed('1'))
one.grid(row=5,column=1,pady=10)

two = Button(window,text="2",padx=100,pady=15,command=lambda: pressed('2'))
two.grid(row=5,column=2,pady=10)

three = Button(window,text="3",padx=100,pady=15,command=lambda: pressed('3'))
three.grid(row=5,column=3,pady=10)

plus = Button(window,text="+",padx=100,pady=15,command=lambda: pressed('+'))
plus.grid(row=5,column=4,pady=10)

reciprocal = Button(window,text="1/x",padx=100,pady=15)
reciprocal.grid(row=6,column=0,pady=10)

plusorminus = Button(window,text="+-",padx=100,pady=15)
plusorminus.grid(row=6,column=1,pady=10)

zero = Button(window,text="0",padx=100,pady=15,command=lambda: pressed('0'))
zero.grid(row=6,column=2,pady=10)

point = Button(window,text=".",padx=100,pady=15,command=lambda: pressed('.'))
point.grid(row=6,column=3,pady=10)

equals = Button(window,text="=",padx=100,pady=15,command=lambda: equal())
equals.grid(row=6,column=4,pady=10)


window.mainloop()
