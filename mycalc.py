from tkinter import *
import math  
window = Tk()

#CODE FOR WINDOW CREATION
window.title("Calculator")
window.geometry("300x300")
inp = Entry(window,width="32")
inp.grid(row=0,column=0,columnspan=4)


#FUNCTIONS
calc = 0.0
math_op = ''
def num_btn_clk(val):
    global calc
    if val!="AC":
        val1= inp.get()+val
        inp.delete(0,"end")
        inp.insert(0,val1)
    else :
        inp.delete(0,"end")
        calc = 0.0

def math_btn_clk(value):
    global calc
    global math_op
    try:
        if value != '=':
            calc = float(inp.get())
            print("Calc is",calc)
            inp.delete(0,"end")
            
        if value == '+':
            math_op = '+'
        elif value == '-':
            math_op = '-'
        elif value == '*':
            math_op = '*'
        elif value == '/':
            math_op = '/'
        elif value == 'SQRT':
            math_op = 'SQRT'
        elif value == '^':
            math_op = '^'
        elif value == '=':
            print("First Number: ",calc,"Second Number: ",inp.get())
            if math_op == '+':
                ans = calc + float(inp.get())
            elif math_op == '-':
                ans = calc - float(inp.get())
            elif math_op == '*':
                ans = calc * float(inp.get())
            elif math_op == '/':
                ans = calc / float(inp.get())
            elif math_op == 'SQRT':
                ans = math.sqrt(calc)
            elif math_op == '^':
                ans = pow(calc,float(inp.get()))
            inp.delete(0,"end")
            if math_op!='':
                inp.insert(0,str(ans))

    except ValueError:
        print("Wrong value","calc",calc,"Math Operator ",math_op)
        inp.delete(0,"end")
    

#CODE FOR BUTTON CREATION
btn7 = Button(window,text="7",command=lambda: num_btn_clk("7"),height=2,width=5).grid(row=1,column=0,padx=2,pady=2)
btn8 = Button(window,text="8",command=lambda: num_btn_clk("8"),height=2,width=5).grid(row=1,column=1,padx=2,pady=2)
btn9 = Button(window,text="9",command=lambda: num_btn_clk("9"),height=2,width=5).grid(row=1,column=2,padx=2,pady=2)
btndiv = Button(window,text="/",command=lambda:math_btn_clk("/"),height=2,width=5).grid(row=1,column=3,padx=2,pady=2)

btn4 = Button(window,text="4",command=lambda: num_btn_clk("4"),height=2,width=5).grid(row=2,column=0,padx=2,pady=2)
btn5 = Button(window,text="5",command=lambda: num_btn_clk("5"),height=2,width=5).grid(row=2,column=1,padx=2,pady=2)
btn6 = Button(window,text="6",command=lambda: num_btn_clk("6"),height=2,width=5).grid(row=2,column=2,padx=2,pady=2)
btnmul = Button(window,text="*",command=lambda:math_btn_clk("*"),height=2,width=5).grid(row=2,column=3,padx=2,pady=2)

btn1 = Button(window,text="1",command=lambda: num_btn_clk("1"),height=2,width=5).grid(row=3,column=0,padx=2,pady=2)
btn2 = Button(window,text="2",command=lambda: num_btn_clk("2"),height=2,width=5).grid(row=3,column=1,padx=2,pady=2)
btn3 = Button(window,text="3",command=lambda: num_btn_clk("3"),height=2,width=5).grid(row=3,column=2,padx=2,pady=2)
btnsub = Button(window,text="-",command=lambda:math_btn_clk("-"),height=2,width=5).grid(row=3,column=3,padx=2,pady=2)

btn0 = Button(window,text="0",command=lambda: num_btn_clk("0"),height=2,width=5).grid(row=4,column=0,padx=2,pady=2)
btndot = Button(window,text=".",command=lambda: num_btn_clk("."),height=2,width=5).grid(row=4,column=1,padx=2,pady=2)
btnequ = Button(window,text="=",command=lambda:math_btn_clk("="),height=2,width=5).grid(row=4,column=2,padx=2,pady=2)
btnsum = Button(window,text="+",command=lambda:math_btn_clk("+"),height=2,width=5).grid(row=4,column=3,padx=2,pady=2)

btnAC = Button(window,text="AC",command=lambda: num_btn_clk("AC"),height=2,width=5).grid(row=5,column=0,padx=2,pady=2)
btnsqrt = Button(window,text="SQRT",command=lambda: math_btn_clk("SQRT"),height=2,width=5).grid(row=5,column=1,padx=2,pady=2)
btnsqr = Button(window,text="^",command=lambda: math_btn_clk('^'),height=2,width=5).grid(row=5,column=2,padx=2,pady=2)

window.mainloop()
