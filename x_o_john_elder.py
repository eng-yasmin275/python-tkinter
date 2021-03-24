import tkinter as tk

root = tk.Tk()
root.title("XO: PLAYER1")


#x starts
clicked = True
count = 0


#when winning disable all buttons
def disable_all_buttons():
    b1.config(state = tk.DISABLED)
    b2.config(state = tk.DISABLED)
    b3.config(state = tk.DISABLED)
    b4.config(state = tk.DISABLED)
    b5.config(state = tk.DISABLED)
    b6.config(state = tk.DISABLED)
    b7.config(state = tk.DISABLED)
    b8.config(state = tk.DISABLED)
    b9.config(state = tk.DISABLED)
    

#to start the game over    
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked , count
    clicked = True
    count = 0
    
    #building buttons
    b1 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b1))
    b2 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b2))               
    b3 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b3))

    b4 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b4))
    b5 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b5))
    b6 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b6))

    b7 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b7))
    b8 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b8))
    b9 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b9))

    #grid buttons
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    
    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2 )

   

#check if someone wins
def checkwin():
    global winner
    winner = False
    
    #check if X wins
    if  b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" :
        b1.config(bg="sky blue")
        b2.config(bg="sky blue")
        b3.config(bg="sky blue")
        winner = True
        tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER1 WINS")
        disable_all_buttons()
        
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" :
         b4.config(bg="sky blue")
         b5.config(bg="sky blue")
         b6.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER1 WINS")
         disable_all_buttons()
    
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X" :
         b7.config(bg="sky blue")
         b8.config(bg="sky blue")
         b9.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER1 WINS")
         disable_all_buttons()
         
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" :
         b1.config(bg="sky blue")
         b4.config(bg="sky blue")
         b7.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER1 WINS")
         disable_all_buttons()
         
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" :
         b2.config(bg="sky blue")
         b5.config(bg="sky blue")
         b8.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER1 WINS")
         disable_all_buttons()
    
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X" :
         b3.config(bg="sky blue")
         b6.config(bg="sky blue")
         b9.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER1 WINS")
         disable_all_buttons()
    
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X" :
         b1.config(bg="sky blue")
         b5.config(bg="sky blue")
         b9.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER1 WINS")
         disable_all_buttons()
    
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X" :
         b3.config(bg="sky blue")
         b5.config(bg="sky blue")
         b7.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER1 WINS")
         disable_all_buttons()
    
    
    #check if o wins
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" :
         b1.config(bg="sky blue")
         b2.config(bg="sky blue")
         b3.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER2 WINS")
         disable_all_buttons()
        
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" :
         b4.config(bg="sky blue")
         b5.config(bg="sky blue")
         b6.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER2 WINS")
         disable_all_buttons()
    
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O" :
         b7.config(bg="sky blue")
         b8.config(bg="sky blue")
         b9.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER2 WINS")
         disable_all_buttons()
         
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" :
         b1.config(bg="sky blue")
         b4.config(bg="sky blue")
         b7.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER2 WINS")
         disable_all_buttons()
         
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" :
         b2.config(bg="sky blue")
         b5.config(bg="sky blue")
         b8.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER2 WINS")
         disable_all_buttons()
    
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O" :
         b3.config(bg="sky blue")
         b6.config(bg="sky blue")
         b9.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER2 WINS")
         disable_all_buttons()
    
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O" :
         b1.config(bg="sky blue")
         b5.config(bg="sky blue")
         b9.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER2 WINS")
         disable_all_buttons()
    
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O" :
         b3.config(bg="sky blue")
         b5.config(bg="sky blue")
         b7.config(bg="sky blue")
         winner = True
         tk.messagebox.showinfo("XO GAME ","CONGRATULATION ..  PLAYER2 WINS")
         disable_all_buttons()
    
    #check if tie
    if count == 9 and winner == False :
        tk.messagebox.showinfo("XO GAME ","IT IS A TIE \n NO ONE WINS" )
        disable_all_buttons()

#button clicked function
def bclick(b):
    global clicked
    global count 
    if b["text"]==" " and clicked == True :
        b["text"] = "X"
        clicked = False
        count += 1
        checkwin()
        root.title("XO: PLAYER2")
        
    elif b["text"]==" " and clicked == False :
         b["text"] = "O"
         clicked = True
         count += 1
         checkwin()
         root.title("XO: PLAYER1")
         
    else:
        tk.messagebox.showerror("XO GAME","THAT BOX HAS BEEN ALREADY SELECTED\n  PICK ANOTHER BOX")
        
    
    
    




#building buttons
b1 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b1))
b2 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b2))               
b3 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b3))

b4 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b4))
b5 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b5))
b6 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b6))

b7 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b7))
b8 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b8))
b9 = tk.Button(root,text=" ",font=("helvetical",20),height=3,width=5,bg="SystemButtonFace",command= lambda: bclick(b9))

#grid buttons
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2 )

#menu creation
my_menu = tk.Menu(root)
root.config(menu=my_menu)

#menu options
options_menu = tk.Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="OPTIONS",menu=options_menu)
options_menu.add_command(label="RESET GAME",command=reset)

reset()
root.mainloop()


