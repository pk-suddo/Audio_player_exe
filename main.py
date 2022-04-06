from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
from tkinter import PhotoImage

current_volume = float(0.5)
root = Tk()
root.geometry("600x500")
root.title("Music Player")
root.configure(background="#95D1CC")


# Functions
def play_song():
    filename = filedialog.askopenfilename(initialdir="C:/", title="Please select a file")
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]
    print(song_title)

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="Blue", text=f"Now Playing: {song_title}")
        volume_label.config(fg="Blue", text=f"Volume: {current_volume * 100}")

    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Error while playing track")


def reduce_volume():
    try:
        global current_volume
        if current_volume <= 0:
            volume_label.config(fg="red", text="Volume : Muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text=f"Volume: {current_volume * 100}")
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn't been selected yet.")


def increase_volume():
    try:
        global current_volume
        if current_volume >= 1:
            volume_label.config(fg="red", text="Volume : Max")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text=f"Volume: {current_volume * 100}")
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn't been selected yet.")


def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn't been selected yet.")


def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Track hasn't been selected yet.")


# labels
Label(root, text="Audio Player", font=("calibre", 44), fg="#1B1A17", bg="#95D1CC").grid(sticky="N", row=0, padx=100, pady=100)
Label(root, text="Please select a music track you would like to play", font=("calibre", 12), fg="black", bg="#95D1CC") \
    .grid(sticky="N", row=1, padx=150)
Label(root, text="Volume", font=("calibre", 15), fg="#151D3B", bg="#95D1CC").grid(sticky="N", row=4, padx=150)

song_title_label = Label(root, font=("calibre", 12), bg="#95D1CC")
song_title_label.grid(sticky="N", row=3)
volume_label = Label(root, font=("Calibre", 12), bg="#95D1CC")
volume_label.grid(sticky="N", row=5)

# Buttons
Button(root, text="Please select a song", bg="red", font=("calibre", 12), command=play_song).grid(row=2, sticky="N")
Button(root, text="Pause", font=("calibre", 15), command=pause).grid(row=3, sticky="E", padx=20)
Button(root, text="Resume", font=("calibre", 15), command=resume).grid(row=3, sticky="W", padx=20)
Button(root, text="+", font=("calibre", 15), width=5, height=2, command=increase_volume).grid(row=5, sticky="E",
                                                                                              padx=20)
Button(root, text="-", font=("calibre", 15), width=5, height=2, command=reduce_volume).grid(row=5, sticky="W",
                                                                                            padx=20)

root.mainloop()
