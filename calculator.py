from  tkinter import *
import tkinter.messagebox
#=======================  Settings  ========================
root=Tk()
root.title('calculator')
root.geometry('400x200')
root.resizable(width=False,height=False)
color='gray'
root.configure(bg=color)

#=======================  Functions  ========================
def errorMsg(ms):
    
    if ms=='error':
        tkinter.messagebox.showerror('Error','something want wrong')
    if ms=='division error':    
        tkinter.messagebox.showerror('Error','Can Not Division By 0')
def plus():
    try:
        value=float(num1.get())+float(num1.get())
        res_value.set(value)
    except:
        errorMsg('error')    
def minus():
    try:
        value=float(num1.get())-float(num1.get())
        res_value.set(value)
    except:
        errorMsg('error') 
def mul():
    try:
        value=float(num1.get())*float(num1.get())
        res_value.set(value)
    except:
        errorMsg('error') 
def div():
    if num2.get()=='0':
        errorMsg('division error')
     
    try:
        value=float(num1.get())/float(num1.get())
        res_value.set(value)
    except:
        errorMsg('error')  
#=======================  Variables  ========================

num1=StringVar()
num2=StringVar()
res_value=StringVar()
#=======================  Frames  ========================

top_first=Frame(root,width=400,height=50,bg=color)
top_first.pack(side=TOP)

top_second=Frame(root,width=400,height=50,bg=color)
top_second.pack(side=TOP)

top_third=Frame(root,width=400,height=50,bg=color)
top_third.pack(side=TOP)

top_forth=Frame(root,width=400,height=50,bg=color)
top_forth.pack(side=TOP)
#=======================  Button  ========================

btn_plus=Button(top_third,text='+',width=8,command=lambda:plus())
btn_plus.pack(side=LEFT,padx=10,pady=5)

btn_minus=Button(top_third,text='-',width=8,command=lambda:minus())
btn_minus.pack(side=LEFT,padx=10,pady=5)

btn_mul=Button(top_third,text='*',width=8,command=lambda:mul())
btn_mul.pack(side=LEFT,padx=10,pady=5)

btn_div=Button(top_third,text='/',width=8,command=lambda:div())
btn_div.pack(side=LEFT,padx=10,pady=5)
#=======================  Entrys And Labels  ========================
label_first_num=Label(top_first,text="Input Number 1 :")
label_first_num.pack(side=LEFT,padx=5,pady=5)
first_num=Entry(top_first,textvariable=num1)
first_num.pack(side=LEFT,pady=5)

label_second_num=Label(top_second,text="Input Number 2 :")
label_second_num.pack(side=LEFT,padx=5,pady=5)
second_num=Entry(top_second,textvariable=num2)
second_num.pack(side=LEFT,pady=5)

res=Label(top_forth,text="Result :")
res.pack(side=LEFT,padx=5,pady=5)
res_num=Entry(top_forth,textvariable=res_value)
res_num.pack(side=LEFT,pady=5)







root.mainloop()