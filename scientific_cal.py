from tkinter import *
import math as m

def click_button(numbers):
                global operator
                operator +=str(numbers)   
                text_Input.set(operator)

def clear_button():
                global operator
                operator=""
                text_Input.set(operator)

def equal_button():
                global operator
                sumup=str(eval(operator))  
                text_Input.set(sumup)
                operator=""

def pi():
    global operator
    operator=str(m.pi)
    text_Input.set(operator)

# def E():
#     text_Input.set(str(m.e)) 

def E():
    global operator
    operator =str(m.e)
    text_Input.set(operator)

def log2():
    global operator
    operator=str(m.log2(int(text_Input.get())))
    text_Input.set(operator)

def log10():
    global operator
    operator=str(m.log10(int(text_Input.get())))
    text_Input.set(operator)
    
def Sin():
    global operator
    operator=str(m.sin(m.radians(int(text_Input.get()))))
    text_Input.set(operator)

def Cos():
    global operator
    operator=str(m.cos(m.radians(int(text_Input.get()))))
    text_Input.set(operator)

def Tan():
    global operator
    operator=str(m.tan(m.radians(int(text_Input.get()))))
    text_Input.set(operator)

def Log():
    global operator
    operator=str(m.log(int(text_Input.get())))
    text_Input.set(operator)
    
def Fact():
    global operator
    operator=str(m.factorial(int(text_Input.get())))
    text_Input.set(operator)
    
def Sqrt():
    global operator
    operator=str(m.sqrt(int(text_Input.get())))
    text_Input.set(operator)  
    
def Square():
    global operator
    operator=str(int(text_Input.get())**2)
    text_Input.set(operator) 
    
def Cube():
    global operator
    operator=str(int(text_Input.get())**3)
    text_Input.set(operator) 
    
def Exp():
    global operator
    operator=str(m.exp(int(text_Input.get())))
    text_Input.set(operator)
    
def Cube():
    global operator
    operator=str(int(text_Input.get())**3)
    text_Input.set(operator)
    
cal=Tk()
cal.title("scientific Calculator")
cal.configure(bg="#393F3A")
operator=""
text_Input=StringVar()
############################################################################

##entry

textDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,width=45,bd=8,
                  insertwidth=3,fg="cyan",bg='black',justify='right').grid(columnspan=7)

############################################################################

##row=1
button_fact=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,bg="black",fg='cyan',font=('arial',14,'bold'),text='x!'
               ,command=lambda:Fact())
button_fact.grid(row=1,column=0)
button_sqrt=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,bg="black",fg='cyan',font=('arial',14,'bold'),text='√x'
               ,command=lambda:Sqrt())
button_sqrt.grid(row=1,column=1)
button_exp=Button(cal,padx=30,pady=8,bd=6,width=3,height=1,bg="black",fg='cyan',font=('arial',14,'bold'),text='e^x'
               ,command=lambda:Exp())
button_exp.grid(row=1,column=2)
button_mod=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,bg="black",fg='cyan',font=('arial',14,'bold'),text='%'
               ,command=lambda:click_button("%"))
button_mod.grid(row=1,column=3)

button_pi=Button(cal,padx=32,pady=8,bd=6,fg="white",bg='black',width=3,height=1,font=('arial',14,'bold'),text='∏'
               ,command=lambda:pi())
button_pi.grid(row=1,column=4)
button_sin=Button(cal,padx=32,pady=8,bd=6,fg="white",bg='black',width=3,height=1,font=('arial',14,'bold'),text='sin'
               ,command=lambda:Sin())
button_sin.grid(row=1,column=5)


##########################################################################################
##row=2

button7=Button(cal,padx=32,pady=8,bd=6,fg="white",bg='black',width=3,height=1,font=('arial',14,'bold'),text='7'
               ,command=lambda:click_button(7))
button7.grid(row=2,column=0)
button8=Button(cal,padx=32,pady=8,bd=6,fg="white",bg='black',width=3,height=1,font=('arial',14,'bold'),text='8'
               ,command=lambda:click_button(8))
button8.grid(row=2,column=1)
button9=Button(cal,padx=32,pady=8,bd=6,fg="white",bg='black',width=3,height=1,font=('arial',14,'bold'),text='9'
               ,command=lambda:click_button(9))
button9.grid(row=2,column=2)
buttonAdd=Button(cal,padx=32,pady=8,bd=6,fg="cyan",bg='black',width=3,height=1,font=('arial',14,'bold'),text='+'
               ,command=lambda:click_button("+"))
buttonAdd.grid(row=2,column=3)
button_e=Button(cal,padx=32,pady=8,width=3,height=1,bd=6,fg="white",bg='black',font=('arial',14,'bold'),text='e'
               ,command=lambda:E())
button_e.grid(row=2,column=4)

button_cos=Button(cal,padx=32,pady=8,width=3,height=1,bd=6,fg="white",bg='black',font=('arial',14,'bold'),text='cos'
               ,command=lambda:Cos())
button_cos.grid(row=2,column=5)
###############################################################################################

#row=3

button4=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,fg="white",bg='black',font=('arial',14,'bold'),text='4'
               ,command=lambda:click_button(4))
button4.grid(row=3,column=0)
button5=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,fg="white",bg='black',font=('arial',14,'bold'),text='5'
               ,command=lambda:click_button(5))
button5.grid(row=3,column=1)
button6=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,fg="white",bg='black',font=('arial',14,'bold'),text='6'
               ,command=lambda:click_button(6))
button6.grid(row=3,column=2)
buttonSub=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,fg="cyan",bg='black',font=('arial',14,'bold'),text='-'
               ,command=lambda:click_button("-"))
buttonSub.grid(row=3,column=3)
button_log2=Button(cal,padx=32,pady=8,bd=6,fg="white",bg='black',width=3,height=1,font=('arial',14,'bold'),text='log2'
               ,command=lambda:log2())
button_log2.grid(row=3,column=4)

button_tan=Button(cal,padx=32,pady=8,bd=6,fg="white",bg='black',width=3,height=1,font=('arial',14,'bold'),text='tan'
               ,command=lambda:Tan())
button_tan.grid(row=3,column=5)

###################################################################################################

#row=4

button1=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,fg="white",bg='black',font=('arial',14,'bold'),text='1'
               ,command=lambda:click_button(1))
button1.grid(row=4,column=0)
button2=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,fg="white",bg='black',font=('arial',14,'bold'),text='2'
               ,command=lambda:click_button(2))
button2.grid(row=4,column=1)
button3=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,fg="white",bg='black',font=('arial',14,'bold'),text='3'
               ,command=lambda:click_button(3))
button3.grid(row=4,column=2)
buttonMul=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,fg="cyan",bg='black',font=('arial',14,'bold'),text='x'
               ,command=lambda:click_button("*"))
buttonMul.grid(row=4,column=3)

button_log10=Button(cal,padx=32,pady=8,bd=6,fg="white",bg='black',width=3,height=1,font=('arial',14,'bold'),text='log10'
               ,command=lambda:log10())
button_log10.grid(row=4,column=4)
button_Square=Button(cal,padx=32,pady=8,bd=6,fg="white",bg='black',font=('arial',14,'bold'),text='x^2'
               ,command=lambda:Square())
button_Square.grid(row=4,column=5)

                   
###################################################################################################

#row=5
button0=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,fg="cyan",bg='black',font=('arial',14,'bold'),text='0'
               ,command=lambda:click_button(0))
button0.grid(row=5,column=0)

buttonClr=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,fg="cyan",bg='black',font=('arial',14,'bold'),text='C'
               ,command=clear_button)
buttonClr.grid(row=5,column=1)
buttonEql=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,fg="cyan",bg='black',font=('arial',14,'bold'),text='='
               ,command=equal_button)
buttonEql.grid(row=5,column=2)
buttondiv=Button(cal,padx=32,pady=8,bd=6,width=3,height=1,fg="cyan",bg='black',font=('arial',14,'bold'),text='/'
               ,command=lambda:click_button("/"))
buttondiv.grid(row=5,column=3)
button_log=Button(cal,padx=32,pady=8,bd=6,fg="white",bg='black',width=3,height=1,font=('arial',14,'bold'),text='log'
               ,command=lambda:Log())
button_log.grid(row=5,column=4)

button_Cube=Button(cal,padx=32,pady=8,bd=6,fg="white",bg='black',width=3,height=1,font=('arial',14,'bold'),text='x^3'
               ,command=lambda:Cube())
button_Cube.grid(row=5,column=5)

cal.mainloop()


