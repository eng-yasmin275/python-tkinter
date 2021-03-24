import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
#root.geometry("320x500")
root.title("MY IMAGE VIEWER")

img1 = ImageTk.PhotoImage(Image.open("images/cat1.jpg")) 
img2 = ImageTk.PhotoImage(Image.open("images/cat2.jpg")) 
img3 = ImageTk.PhotoImage(Image.open("images/cat3.jpg")) 
img4 = ImageTk.PhotoImage(Image.open("images/cat4.jpg")) 
img5 = ImageTk.PhotoImage(Image.open("images/cat5.jpg")) 

imglist = [img1,img2,img3,img4,img5]
status = tk.Label(root,text="image 1 of "+ str(len(imglist)),bd=1,relief=tk.SUNKEN,anchor="e")

my_label = tk.Label(image = img1)
my_label.grid(row=0,column=0,columnspan=3)

def back(img_number):
    global my_label
    global buttonback
    global buttonforward
    
    my_label.grid_forget()
    my_label = tk.Label(image=imglist[img_number-1])
    buttonforward = tk.Button(root,text=">>",command=lambda:forward(img_number+1))
    buttonback = tk.Button(root,text="<<",command=lambda:back(img_number-1))
    if img_number == 1:
        buttonback = tk.Button(root,text="<<",state=tk.DISABLED)
    
    my_label.grid(row=0,column=0,columnspan=3)
    buttonback.grid(row=1,column=0)
    buttonforward.grid(row=1,column=2)
    status = tk.Label(root,text="image "+str(img_number)+" of "+ str(len(imglist)),bd=1,relief=tk.SUNKEN,anchor="e")
    status.grid(row=2,column=0,columnspan=3,sticky="E"+"W")
    

def forward(img_number):
    global my_label
    global buttonback
    global buttonforward
    
    my_label.grid_forget()
    my_label = tk.Label(image=imglist[img_number-1])
    buttonforward = tk.Button(root,text=">>",command=lambda:forward(img_number+1))
    buttonback = tk.Button(root,text="<<",command=lambda:back(img_number-1))
    if img_number == 5:
        buttonforward = tk.Button(root,text=">>",state=tk.DISABLED)
    
    
    my_label.grid(row=0,column=0,columnspan=3)
    buttonback.grid(row=1,column=0)
    buttonforward.grid(row=1,column=2)
    
    status = tk.Label(root,text="image "+str(img_number)+" of "+ str(len(imglist)),bd=1,relief=tk.SUNKEN,anchor="e")
    status.grid(row=2,column=0,columnspan=3,sticky="E"+"W")


buttonback = tk.Button(root,text="<<",command=back,state=tk.DISABLED)
buttonexit = tk.Button(root,text="EXIT",command=root.destroy)
buttonforward = tk.Button(root,text=">>",command=lambda:forward(2))

buttonback.grid(row=1,column=0)
buttonexit.grid(row=1,column=1)
buttonforward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky="E"+"W")

root.mainloop()