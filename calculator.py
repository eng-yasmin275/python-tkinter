import tkinter as tk
root = tk.Tk()

root.title("SIMPLE CALCULATOR")
e = tk.Entry(root,width=45,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def buttonclick(number):
    current = e.get()
    e.delete(0,tk.END)
    e.insert(0,str(current) + str(number))
    
def buttonclear():
    e.delete(0,tk.END)
    
def buttonadd():
    first_number = e.get()
    global f_number 
    global math
    math = "add"
    f_number= int(first_number)
    e.delete(0,tk.END)
    

    
def buttonsubtract():
    first_number = e.get()
    global f_number 
    global math
    math = "sub"
    f_number= int(first_number)
    e.delete(0,tk.END)

def buttonmultiply():
    first_number = e.get()
    global f_number 
    global math
    math = "mult"
    f_number= int(first_number)
    e.delete(0,tk.END)

def buttondivide():
    first_number = e.get()
    global f_number 
    global math
    math = "div"
    f_number= int(first_number)
    e.delete(0,tk.END)
    
    
def buttonequal():
    second_number = e.get()
    e.delete(0,tk.END)
    
    if math == "add":
        e.insert(0,f_number + int(second_number))
        
    if math == "sub":
        e.insert(0,f_number - int(second_number))
        
    if math == "mult":
        e.insert(0,f_number * int(second_number))
        
    if math == "div":
        e.insert(0,f_number / int(second_number))


#define buttons
button1 = tk.Button(root,text="1",padx=40,pady=20,command=lambda:buttonclick(1))
button2 = tk.Button(root,text="2",padx=40,pady=20,command=lambda:buttonclick(2))
button3 = tk.Button(root,text="3",padx=40,pady=20,command=lambda:buttonclick(3))
button4 = tk.Button(root,text="4",padx=40,pady=20,command=lambda:buttonclick(4))
button5 = tk.Button(root,text="5",padx=40,pady=20,command=lambda:buttonclick(5))
button6 = tk.Button(root,text="6",padx=40,pady=20,command=lambda:buttonclick(6))
button7 = tk.Button(root,text="7",padx=40,pady=20,command=lambda:buttonclick(7))
button8 = tk.Button(root,text="8",padx=40,pady=20,command=lambda:buttonclick(8))
button9 = tk.Button(root,text="9",padx=40,pady=20,command=lambda:buttonclick(9))
button0 = tk.Button(root,text="0",padx=40,pady=20,command=lambda:buttonclick(0))
button_add = tk.Button(root,text="+",padx=39,pady=20,command=buttonadd)
button_subtract = tk.Button(root,text="-",padx=39,pady=20,command=buttonsubtract)
button_multiply = tk.Button(root,text="*",padx=39,pady=20,command=buttonmultiply)
button_divide= tk.Button(root,text="/",padx=39,pady=20,command=buttondivide)
button_equal = tk.Button(root,text="=",padx=91,pady=20,command=buttonequal)
button_clear = tk.Button(root,text="CLEAR",padx=79,pady=20,command=buttonclear)

#put buttons on screen
button1.grid(row=3 ,column=0)
button2.grid(row=3 ,column=1)
button3.grid(row=3 ,column=2)
button4.grid(row=2 ,column=0)
button5.grid(row=2 ,column=1)
button6.grid(row=2 ,column=2)
button7.grid(row=1 ,column=0)
button8.grid(row=1 ,column=1)
button9.grid(row=1 ,column=2)
button0.grid(row=4 ,column=1)
button_add.grid(row=4,column=0)
button_subtract.grid(row=4,column=2)
button_multiply.grid(row=5,column=0)
button_divide.grid(row=6,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=6,column=1,columnspan=2)





root.mainloop()