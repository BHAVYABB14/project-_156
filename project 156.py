from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title("Endless Pokemon Game")
root.geometry("620x460")

root.configure(background = "orange")

abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasaur"))
charmender = ImageTk.PhotoImage(Image.open("charmender"))
iyvasour = ImageTk.PhotoImage(Image.open("iyvasour"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra"))
meowth = ImageTk.PhotoImage(Image.open("meowth"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking"))
paras = ImageTk.PhotoImage(Image.open("paras"))
persion = ImageTk.PhotoImage(Image.open("persion"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu"))
ratata = ImageTk.PhotoImage(Image.open("ratata"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle"))


player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score_label = Label(root, bg = "royal blue", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root, bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_pc_label = Label(root, bg = "white", fg = "orange")
random_pc_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()