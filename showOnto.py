#library_getter
from owlready2 import *
from tkinter import *
from functools import partial
owlready2.JAVA_EXE = "C:\\Users\\maksy\\.jdks\\jdk-19.0.2\\bin\\java.exe"


def color_config(widget, color, event):
    widget.configure(foreground=color)

root = Tk()
root.geometry("700x500")
frm = root

bod = Frame(frm, width=600, highlightbackground="black", highlightthickness=1)
bod.pack(padx=20, pady=20, fill="x")

bod.grid_rowconfigure(0, weight=1)
bod.grid_columnconfigure(0, weight=1)
bod.grid_columnconfigure(1, weight=1)
bod.grid_columnconfigure(2, weight=1)

top_left = Frame(bod, highlightbackground="black", highlightthickness=1)
top_left.grid(column=0, row=0, sticky=NSEW)

top_center = Frame(bod, highlightbackground="black", highlightthickness=1)
top_center.grid(column=1, row=0, sticky=NSEW)

top_right = Frame(bod, highlightbackground="black", highlightthickness=1)
top_right.grid(column=2, row=0, sticky=NSEW)

bottom = Frame(bod, highlightbackground="black", highlightthickness=1)
bottom.grid(column=0, row=1, columnspan=3, sticky=NSEW)

songs = Frame(top_left)
songs.pack(anchor="nw", padx=5, pady=10)

albums = Frame(top_center)
albums.pack(anchor="nw", padx=5, pady=10)

artists = Frame(top_right)
artists.pack(anchor="nw", padx=5, pady=10)

info = Frame(bottom)
info.grid(column=0, row=0, padx=10, pady=5, sticky=NW)

onto = get_ontology("./onto.owl").load()
library = onto.get_namespace("http://test.org/onto.owl")


sync_reasoner()



def showInfo(song):
    for widget in info.winfo_children():
        widget.destroy()

    Label(info, text=song.name, font=("Comic Sans", 10), justify="left").pack( anchor="nw")

    for c in song.is_a:
        try:
            Label(info, text="*" + c.label[0], justify="left").pack( anchor="nw")
        except:
            pass

    for prop in song.get_properties():
        Label(info, text= prop.label[0] + ": ", justify="left").pack( anchor="nw")
        for value in prop[song]:
            Label(info, text="* " +  value.name , justify="left").pack( anchor="nw", padx=10)

    
text1 = Label(songs, text="Songs:", font=("Comic Sans", 10))
text1.pack(anchor="nw")

for song in library.Song.instances():
    text = Label(songs, text=song.name, font=("Comic Sans", 10), fg="blue", cursor="hand2")
    text.pack(anchor="nw")
    text.bind("<Enter>", partial(color_config, text, "red"))
    text.bind("<Leave>", partial(color_config, text, "blue"))
    text.bind("<Button-1>", lambda e, song=song:showInfo(song))

text2 = Label(albums, text="Albums:", font=("Comic Sans", 10))
text2.pack(anchor="nw")

for album in library.Album.instances():
    text = Label(albums, text=album.name, font=("Comic Sans", 10), fg="blue", cursor="hand2")
    text.pack(anchor="nw")
    text.bind("<Enter>", partial(color_config, text, "red"))
    text.bind("<Leave>", partial(color_config, text, "blue"))
    text.bind("<Button-1>", lambda e, album=album:showInfo(album))

text3 = Label(artists, text="Artists we have:", font=("Comic Sans", 10))
text3.pack(anchor="nw")

for artist in library.Artist.instances():
    text = Label(artists, text=artist.name, font=("Comic Sans", 10), fg="blue", cursor="hand2")
    text.pack(anchor="nw")
    text.bind("<Enter>", partial(color_config, text, "red"))
    text.bind("<Leave>", partial(color_config, text, "blue"))
    text.bind("<Button-1>", lambda e, artist=artist:showInfo(artist))


root.mainloop()




