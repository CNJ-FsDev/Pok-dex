from tkinter import *
from io import BytesIO

import PIL.Image
import PIL.ImageTk
import pypokedex
import urllib3

from PIL import Image, ImageTk
from HoverClass import HoverInfo
from tkinter import filedialog


# file explorer window
# image uploader function
def imageUploader():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=fileTypes)

    # if file is selected
    if len(path):
        img = Image.open(path)
        img = img.resize((320, 500))
        pic = ImageTk.PhotoImage(img)

        bg_lbl.config(image=pic)
        bg_lbl.image = pic

    # if no file is selected, then we are displaying below message
    else:
        print("No file is Choosen !! Please choose a file.")


# Window
window = Tk()
window.geometry("400x600")
window.title("Pokémon")
icon = PhotoImage(file='Images/pokeball.png')  # windows icon using a local file
window.iconphoto(True, icon)
window.config(padx=5,
              pady=15,
              background="red",
              relief=RAISED,
              bd=35)

# Background image
bg = Image.open('Images/background.png')
resized_bg = bg.resize((320, 500), Image.Resampling.LANCZOS)
bg2 = ImageTk.PhotoImage(resized_bg)

bg_lbl = Label(window,
               bg="white",
               fg="black",
               image=bg2)
bg_lbl.pack()


# Title
title_label = Label(window,
                    text="Desktop Pokédex",
                    font=("Arial Bold", 15),
                    bg="red",
                    fg="blue",
                    relief=RAISED,
                    bd=10,
                    padx=5,
                    pady=5,
                    compound='left')
title_label.place(x=60, y=10)

# Container frame - Pokedex
container = Frame(window)
container.pack(fill=BOTH, expand=True)
# Image Canvas - Pokemon Image
image_icon = Canvas(window,
                    bg="black",
                    relief=RAISED,
                    bd=10,
                    width=150,
                    height=150)
image_icon.place(x=10, y=140)

pokemon_image = Label(image_icon)
pokemon_image.pack(padx=10, pady=10)

# Pokemon ID / Name
p_name = Label(window,
               text="Pokémon ID/Name:",
               font=("Arial Bold", 10),
               bg="red",
               fg="yellow",
               relief=RAISED,
               bd=10,
               padx=10,
               pady=1,
               width=14,
               anchor="center")
p_name.place(x=150, y=140)
# Pokemon ID / Name Response
pokemon_information = Label(window,
                            font=("Arial Bold", 10),
                            bg="red",
                            fg="blue",
                            relief=RAISED,
                            bd=10,
                            padx=10,
                            pady=1,
                            width=14,
                            anchor="center")
pokemon_information.place(x=150, y=180)
# Pokemon Type
p_name = Label(window,
               text="Pokémon Type:",
               font=("Arial Bold", 10),
               bg="red",
               fg="yellow",
               relief=RAISED,
               bd=10,
               padx=10,
               pady=1,
               width=14,
               anchor="center")
p_name.place(x=150, y=220)
# Pokemon Type Response
pokemon_types = Label(window,
                      font=("Arial Bold", 10),
                      bg="red",
                      fg="blue",
                      relief=RAISED,
                      bd=10,
                      padx=10,
                      pady=1,
                      width=14,
                      anchor="center")
pokemon_types.place(x=150, y=260)

# Div bar
div = Label(window,
            bg="yellow",
            relief=RAISED,
            bd=8,
            width=42,
            anchor="center")
div.place(x=5, y=310)

# Pokemon abilities
abilities = Label(window, text="Moves",
                  font=("Arial Bold", 10),
                  bg="red",
                  fg="yellow",
                  relief=RAISED,
                  bd=10,
                  padx=10,
                  pady=1,
                  width=14,
                  anchor="center")
abilities.place(x=80, y=360)
# AB1
ability1 = Label(window,
                 text="----",
                 font=("Arial Bold", 10),
                 bg="red",
                 fg="black",
                 relief=RAISED,
                 bd=10,
                 padx=10,
                 pady=1,
                 width=14,
                 anchor="center")
ability1.place(x=5, y=405)
# AB2
ability2 = Label(window,
                 text="----",
                 font=("Arial Bold", 10),
                 bg="red",
                 fg="black",
                 relief=RAISED,
                 bd=10,
                 padx=10,
                 pady=1,
                 width=14,
                 anchor="center")
ability2.place(x=165, y=405)
# AB3
ability3 = Label(window,
                 text="----",
                 font=("Arial Bold", 10),
                 bg="red",
                 fg="black",
                 relief=RAISED,
                 bd=10,
                 padx=10,
                 pady=1,
                 width=14,
                 anchor="center")
ability3.place(x=5, y=450)
# AB4
ability4 = Label(window,
                 text="----",
                 font=("Arial Bold", 10),
                 bg="red",
                 fg="black",
                 relief=RAISED,
                 bd=10,
                 padx=10,
                 pady=1,
                 width=14,
                 anchor="center")
ability4.place(x=165, y=450)


# Function to get the Pokémon from user input of the Pokémon id number or name
def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())

    ability1.config(text=pokemon.abilities[0].name.upper())
    ability2.config(text=pokemon.abilities[1].name.upper())
    print(pokemon.abilities)


# Text Box - User Input
text_id_name = Text(window, height=0)
text_id_name.insert(1.0, "Pikachu")
load_pokemon()
text_id_name.config(font=("Arial Bold", 12),
                    width=22,
                    bg="red",
                    relief=SUNKEN,
                    bd=10)
text_id_name.place(x=10, y=70)

# Button = when clicked, loads Pokémon
btn_load = Button(window,
                  command=load_pokemon,
                  text="Select",
                  font=("Arial Bold", 10),
                  bg="red",
                  fg="blue",
                  relief=RAISED,
                  bd=5,
                  padx=5,
                  pady=5)
btn_load.place(x=240, y=70)

# Button = when clicked, changes background by open an image from the computer system
btn_bg = Button(window,
                  command=imageUploader,
                  text="BG",
                  font=("Arial Bold", 10),
                  bg="green",
                  fg="blue",
                  relief=RAISED,
                  bd=5,
                  padx=5,
                  pady=5)
btn_bg.place(x=280, y=0)
HoverInfo(btn_bg, 'Change background image.')


window.mainloop()
