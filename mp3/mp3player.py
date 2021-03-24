import tkinter as tk
import pygame
from tkinter import filedialog  #to add songs to song box

root = tk.Tk()
root.title("MY MP3 PLAYER")
root.iconbitmap("C:/Users\hp\Desktop\python\music.ico")
root.geometry("800x500")

#to start pygame mixer
pygame.mixer.init()

#functions
def addonesong():
    song = filedialog.askopenfilename(initialdir="G:\yasmin\yasmin\music\workmood/",title="CHOOSE A SONG",filetypes=(("mp3 Files","*.mp3"), )) 
    #song = song.replace("G:/yasmin/yasmin/music/workmood/","") #elimimnate directory of song
    #song = song.replace(".mp3","") #eliminate extention of song
    song_box.insert(tk.END,song)
    
def play():
    song = song_box.get(tk.ACTIVE)
    #song = f"G:/yasmin/yasmin/music/workmood/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
def stop():
    pygame.mixer.music.stop()
    #song_box.selection_clear(tk.ACTIVE) #if we want to clear song after stop it
    

#create playlist box
song_box = tk.Listbox(root,bg="#CCCCCC",fg="#FF6633",width=200,selectbackground="black")
song_box.pack(pady=20)

#create control buttons images
play_button_img = tk.PhotoImage(file="Play-icon.png")

stop_button_img = tk.PhotoImage(file="Stop-icon.png")

pause_button_img = tk.PhotoImage(file="Pauseicon.png")

forward_button_img = tk.PhotoImage(file="forward-icon.png")

backward_button_img = tk.PhotoImage(file="Backward-icon.png") 


#create control frames
control_frame = tk.Frame(root)
control_frame.pack()

#create control buttons 
play_button = tk.Button(control_frame,image=play_button_img,borderwidth=0,command=play)  #borderwidth=0  to getred of the surrounded image
play_button.grid(row=0,column=1,padx=10)

stop_button = tk.Button(control_frame,image=stop_button_img,borderwidth=0,command=stop)
stop_button.grid(row=0,column=3,padx=10)

pause_button = tk.Button(control_frame,image=pause_button_img,borderwidth=0)
pause_button.grid(row=0,column=2,padx=10)

forward_button = tk.Button(control_frame,image=forward_button_img,borderwidth=0)
forward_button.grid(row=0,column=4,padx=10)

backward_button = tk.Button(control_frame,image=backward_button_img,borderwidth=0)
backward_button.grid(row=0,column=0,padx=10)


#create menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)

#create add song menu
addsong_menu = tk.Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="ADD SONGS",menu=addsong_menu)
addsong_menu.add_command(label="ADD ONE SONG",command=addonesong)





















# #FUNCTIONS
# def play():
#     pygame.mixer.music.load("G:\yasmin\yasmin\music\mustafacecli.mp3")
#     pygame.mixer.music.play()
    
    
# def stop():
#     pygame.mixer.music.stop()
    

# play_button = tk.Button(root,text="PLAY",font=("HELVETCA",32),activeforeground="grey",activebackground="pink",command=play)
# play_button.grid(row=1,column=1,padx=20,pady=20)

# stop_button = tk.Button(root,text="STOP",font=("HELVETCA",32),activeforeground="grey",activebackground="pink",command=stop)
# stop_button.grid(row=1,column=2,padx=20,pady=20)




root.mainloop()