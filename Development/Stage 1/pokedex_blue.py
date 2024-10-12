from tkinter import *
from io import BytesIO

import PIL.Image
import PIL.ImageTk
import pypokedex
import urllib3

# Window
window = Tk()
window.geometry("400x400")
window.minsize(400, 400)
window.maxsize(400, 400)
window.title("Pokémon")
icon = PhotoImage(file='../../Images/pokeball.png')  # windows icon using a local file
window.iconphoto(True, icon)
window.config(padx=5, pady=15, background="blue", relief=RAISED, bd=35)

# Background image
bg = PhotoImage(file='../../Images/img.png')
bg_lbl = Label(window, bg="white", fg="black", image=bg)
bg_lbl.pack()

# Title
title_label = Label(window, text="Desktop Pokédex", font=("Arial Bold", 15), bg="blue", fg="yellow",
                    relief=RAISED, bd=10, padx=5, pady=5, compound='left')
title_label.place(x=60, y=10)

# Container frame - Pokedex
container = Frame(window)
container.pack(fill=BOTH, expand=True)

# Image Canvas - Pokemon Image
image_icon = Canvas(window, bg="black", relief=RAISED, bd=10,
                    width=150, height=150)
image_icon.place(x=10, y=140)
pokemon_image = Label(image_icon)
pokemon_image.pack(padx=10, pady=10)

# Pokemon ID / Name
p_name = Label(window, text="Pokémon ID/Name:", font=("Arial Bold", 10), bg="blue", fg="red",
               relief=RAISED, bd=10, padx=10, pady=1, width=14, anchor="center")
p_name.place(x=150, y=140)
# Pokemon ID / Name Response
pokemon_information = Label(window, font=("Arial Bold", 10), bg="blue", fg="yellow",
                            relief=RAISED, bd=10, padx=10, pady=1, width=14, anchor="center")
pokemon_information.place(x=150, y=180)
# Pokemon Type
p_name = Label(window, text="Pokémon Type:", font=("Arial Bold", 10), bg="blue", fg="red",
               relief=RAISED, bd=10, padx=10, pady=1, width=14, anchor="center")
p_name.place(x=150, y=220)
# Pokemon Type Response
pokemon_types = Label(window, font=("Arial Bold", 10), bg="blue", fg="yellow",
                      relief=RAISED, bd=10, padx=10, pady=1, width=14, anchor="center")
pokemon_types.place(x=150, y=260)


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


# Text Box - User Input
text_id_name = Text(window, height=1)
text_id_name.insert(1.0, "Pikachu")
load_pokemon()
text_id_name.config(font=("Arial", 12), width=22, bg="blue",
                    relief=SUNKEN, bd=10)
text_id_name.place(x=10, y=70)

# Button = when clicked, loads Pokémon
btn_load = Button(window, command=load_pokemon, text="Select", font=("Arial Bold", 10), bg="blue", fg="yellow",
                  relief=RAISED, bd=5, padx=5, pady=5)
btn_load.place(x=240, y=70)

window.mainloop()


