from tkinter import *
from tkinter import ttk
from io import BytesIO

import PIL.Image
import PIL.ImageTk
import pypokedex
import urllib3

from PIL import Image, ImageTk
from HoverClass import HoverInfo
from tkinter import filedialog


class App(Tk):
    def __init__(self, name, xx, yy, icon, colour):
        super().__init__()
        # main setup
        self.title(name)  # Fore Header
        self.geometry(f'{xx}x{yy}')  # Window Size
        # self.minsize(xx, yy)  # Minimum Window size
        # self.maxsize(xx, yy)  # Maximum Window size
        # self.attributes('-fullscreen', True)  # Full Screen Window
        self.icon = PhotoImage(file=icon)  # Window Icon Image
        self.iconphoto(True, self.icon)  # ? ? ?
        self.config(background=colour, relief=RAISED, bd=35, padx=5, pady=15,)  # ? ? ?

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

        # file explorer window
        # image uploader function
        def imageUploader():
            filetypes = [("Image files", "*.png;*.jpg;*.jpeg")]
            path = filedialog.askopenfilename(filetypes=filetypes)

            # if file is selected
            if len(path):
                img = Image.open(path)
                img = img.resize((320, 500))
                pic = ImageTk.PhotoImage(img)

                bg_lbl.config(image=pic)
                bg_lbl.image = pic

            # if no file is selected,
            # then we are displaying below message.
            # print to user-interface instead of terminal.

            else:
                print("No file is Chosen !! Please choose a file.")

        # Theme colour changer
        def theme():
            red = 'red'
            blue = 'blue'
            green = 'green'
            yellow = 'yellow'
            if colourz.get() == ' Red':
                self.config(background=red)
                text_id_name.config(bg=red, fg=blue)
                btn_load.config(bg=red, fg=blue)
                title_label.config(bg=red, fg=blue)
                p_name.config(bg=red, fg=blue)
                p_id.config(bg=red, fg=blue)
                pokemon_information.config(bg=red, fg=blue)
                pokemon_types.config(bg=red, fg=blue)
                div.config(bg=yellow, fg=blue)
                abilities.config(bg=red, fg=blue)
                ability1.config(bg=red, fg=blue)
                ability2.config(bg=red, fg=blue)
                ability3.config(bg=red, fg=blue)
                ability4.config(bg=red, fg=blue)
            elif colourz.get() == ' Blue':
                self.config(background=blue)
                text_id_name.config(bg=blue, fg=red)
                btn_load.config(bg=blue, fg=red)
                title_label.config(bg=blue, fg=red)
                p_name.config(bg=blue, fg=red)
                p_id.config(bg=blue, fg=red)
                pokemon_information.config(bg=blue, fg=red)
                pokemon_types.config(bg=blue, fg=red)
                div.config(bg=green, fg=red)
                abilities.config(bg=blue, fg=red)
                ability1.config(bg=blue, fg=red)
                ability2.config(bg=blue, fg=red)
                ability3.config(bg=blue, fg=red)
                ability4.config(bg=blue, fg=red)
            elif colourz.get() == ' Green':
                self.config(background=green)
                text_id_name.config(bg=green, fg=yellow)
                btn_load.config(bg=green, fg=yellow)
                title_label.config(bg=green, fg=yellow)
                p_name.config(bg=green, fg=yellow)
                p_id.config(bg=green, fg=yellow)
                pokemon_information.config(bg=green, fg=yellow)
                pokemon_types.config(bg=green, fg=yellow)
                div.config(bg=red)
                abilities.config(bg=green, fg=yellow)
                ability1.config(bg=green, fg=yellow)
                ability2.config(bg=green, fg=yellow)
                ability3.config(bg=green, fg=yellow)
                ability4.config(bg=green, fg=yellow)
            elif colourz.get() == ' Yellow':
                self.config(background=yellow)
                text_id_name.config(bg=yellow, fg=green)
                btn_load.config(bg=yellow, fg=green)
                title_label.config(bg=yellow, fg=green)
                p_name.config(bg=yellow, fg=green)
                p_id.config(bg=yellow, fg=green)
                pokemon_information.config(bg=yellow, fg=green)
                pokemon_types.config(bg=yellow, fg=green)
                div.config(bg=blue)
                abilities.config(bg=yellow, fg=green)
                ability1.config(bg=yellow, fg=green)
                ability2.config(bg=yellow, fg=green)
                ability3.config(bg=yellow, fg=green)
                ability4.config(bg=yellow, fg=green)

        # Background image
        bg = Image.open('Images/background.png')
        resized_bg = bg.resize((320, 500), Image.Resampling.LANCZOS)
        bg2 = ImageTk.PhotoImage(resized_bg)

        bg_lbl = Label(self,
                       bg="white",
                       fg="black",
                       image=bg2)
        bg_lbl.pack()

        # Title
        title_label = Label(self,
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
        container = Frame(self)
        container.pack(fill=BOTH, expand=True)
        # Image Canvas - Pokemon Image
        image_icon = Canvas(self,
                            bg="black",
                            relief=RAISED,
                            bd=10,
                            width=150,
                            height=150)
        image_icon.place(x=10, y=140)

        pokemon_image = Label(image_icon)
        pokemon_image.pack(padx=10, pady=10)

        # Pokemon ID / Name
        p_id = Label(self,
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
        p_id.place(x=150, y=140)
        # Pokemon ID / Name Response
        pokemon_information = Label(self,
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
        p_name = Label(self,
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
        pokemon_types = Label(self,
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
        div = Label(self,
                    bg="yellow",
                    relief=RAISED,
                    bd=8,
                    width=42,
                    anchor="center")
        div.place(x=5, y=310)

        # Pokemon abilities
        abilities = Label(self, text="Moves",
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
        ability1 = Label(self,
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
        ability2 = Label(self,
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
        ability3 = Label(self,
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
        ability4 = Label(self,
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

        # Text Box - User Input
        text_id_name = Text(self, height=0)
        text_id_name.insert(1.0, "Pikachu")
        load_pokemon()
        text_id_name.config(font=("Arial Bold", 12),
                            width=22,
                            bg="red",
                            relief=SUNKEN,
                            bd=10)
        text_id_name.place(x=10, y=70)

        # Button = when clicked, loads Pokémon
        btn_load = Button(self,
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
        btn_bg = Button(self,
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

        # Combobox creation
        n = StringVar()
        colourz = ttk.Combobox(self, width=27, textvariable=n)

        # Adding combobox drop down list
        colourz['values'] = (' Red',
                             ' Blue',
                             ' Green',
                             ' Yellow')

        colourz.place(x=0, y=0)
        colourz.current()

        # Button to activate a function to change theme colour
        change = Button(self,
                        command=theme,
                        text="X",
                        font=("Arial Bold", 10),
                        bg="white",
                        fg="blue",
                        relief=RAISED,
                        bd=5,
                        padx=5,
                        pady=5)
        change.place(x=0, y=20)


if __name__ == '__main__':
    app = App('Pokémon', 400, 600, 'Images/pokeball.png', 'red')
    app.mainloop()
