#import library
from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
import random
import time
import os


#initialize window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('DataFlair-Rock,Paper,Scissors')
root.config(bg ='seashell3')

user_wins = 0
comp_wins = 0
msg_lose = "you loose, computer select "
msg_win =  "you win, computer select "

def Reset():
    global user_wins, comp_wins
    Result.set("")
    user_wins = 0
    comp_wins = 0


def UpdateScore():
    global user_wins, comp_wins
    score_str = f"Score: {user_wins} - {comp_wins}"
    score_label.config(text=score_str)


def WinnerExit():
    Result.set("Saliendo en 3 segundos...")
    root.after(3000, root.destroy)

def Exit():
    root.destroy()

def on_click(user_pick):
    global user_wins, comp_wins
    Result.set("")

    comp_pick = random.choice(['rock', 'paper', 'scissors'])
    
    if user_pick == comp_pick:
        Result.set('Tie,you both select same')

    elif user_pick == 'rock':
        if comp_pick == 'paper':
            Result.set(msg_lose + comp_pick)
        elif comp_pick == 'scissors':
            Result.set(msg_win + comp_pick)

    elif user_pick == 'paper':
        if comp_pick == 'scissors':
            Result.set(msg_lose + comp_pick)     
        elif comp_pick == 'rock':
            Result.set(msg_win + comp_pick)      

    elif user_pick == 'scissors':
        if comp_pick == 'rock':
            Result.set(msg_lose + comp_pick)   

        elif comp_pick == 'rock':
            Result.set(msg_win + comp_pick)


    # Actualiza los contadores de victorias   
    if Result.get().startswith('you win'):
        user_wins += 1
    elif Result.get().startswith('you loose'):
        comp_wins += 1        

    # Comprueba si alguien ha ganado
    if user_wins == 3:
        Result.set(f"¡Felicidades! Has ganado el juego!")
        WinnerExit()

    elif comp_wins == 3:
        Result.set(f"Lo siento, la computadora ha ganado el juego.")
        WinnerExit()


    # Actualiza la puntuación en la ventana
    UpdateScore()


#heading
Label(root, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', bg = 'seashell2').pack()


# Score labels
score_label = Label(root, text = 'Score: 0 - 0', font='arial 15 bold', bg = 'seashell2')
score_label.pack()

# Obtener la ruta absoluta del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir rutas absolutas para las imágenes
rock_img_path = os.path.join(script_dir, "rock_img.png")
paper_img_path = os.path.join(script_dir, "paper_img.png")
scissors_img_path = os.path.join(script_dir, "scissors_img.png")

# Cargar imágenes
rock_img = PhotoImage(file=rock_img_path)
paper_img = PhotoImage(file=paper_img_path)
scissors_img = PhotoImage(file=scissors_img_path)

new_width = 50  # Nuevo ancho deseado
new_height = 50  # Nuevo alto deseado
rock_img = rock_img.subsample(int(rock_img.width() / new_width), int(rock_img.height() / new_height))
paper_img = paper_img.subsample(int(paper_img.width() / new_width), int(paper_img.height() / new_height))
scissors_img = scissors_img.subsample(int(scissors_img.width() / new_width), int(scissors_img.height() / new_height))

##user choice
Label(root, text = 'choose any one: rock, paper ,scissors' , font='arial 15 bold', bg = 'seashell2').place(x = 20,y=75)
# Create buttons with images
rock_btn = tk.Button(root, text='Rock', image=rock_img, compound='top', command=lambda: on_click('rock'), width = 100)
rock_btn.place(x = 5,y=180)

paper_btn = tk.Button(root, text='Paper', image=paper_img, compound='top', command=lambda: on_click('paper'), width = 100)
paper_btn.place(x= 135,y=180)

scissors_btn = tk.Button(root, text='Scissors', image=scissors_img, compound='top', command=lambda: on_click('scissors'), width = 100)
scissors_btn.place(x= 265,y=180)

Result = StringVar()
Entry(root, font = 'arial 14 bold', textvariable = Result, bg ='antiquewhite2',width = 38).place(x=5, y = 280)
Button(root, font = 'arial 13 bold', text = 'EXIT' ,padx =5,bg ='seashell4' ,command = Exit).place(x=170,y=330)


# Inicializar contadores de victorias
user_wins = 0
comp_wins = 0

# Ejecutar la interfaz de usuario
root.mainloop()