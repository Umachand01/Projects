import os  # Module to interact with the operating system
import tkinter as tk  # Module for creating GUI applications
from tkinter import filedialog  # Module for file dialog
import pygame  # Module for game development, also used for playing music
import fontstyle  # Presumably for text styling, though not used here

# Define color constants
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray="#646464"

# Initialize pygame mixer for playing music
pygame.mixer.init()

# Set up the main application window
root = tk.Tk()
root.title("Simple MP3 Player")
root.geometry("500x800")

# Function to load music
def load_music():
    global music_file
    # Open file dialog to select an MP3 file
    music_file = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if music_file:
        # Load the selected MP3 file into pygame mixer
        pygame.mixer.music.load(music_file)
        # Set the song title in the GUI
        song_title.set(os.path.basename(music_file))
        # Play the loaded music
        play_music()

# Function to play music
def play_music():
    pygame.mixer.music.play()

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Function to set volume
def set_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

# Creating interface elements with specified styles
load_button = tk.Button(root, text="Load Music", command=load_music,
                        foreground=color_gray, background=color_yellow,
                        width=50, height=4, font=("Helvetica", 16, "bold"))
play_button = tk.Button(root, text="Play", command=play_music,
                        foreground=color_gray, background=color_yellow,
                        width=50, height=4, font=("Helvetica", 16, "bold"))
pause_button = tk.Button(root, text="Pause", command=pause_music,
                         foreground=color_gray, background=color_yellow,
                         width=50, height=4, font=("Helvetica", 16, "bold"))
stop_button = tk.Button(root, text="Stop", command=stop_music,
                        foreground=color_gray, background=color_yellow,
                        width=50, height=4, font=("Helvetica", 16, "bold"))
volume_label = tk.Label(root, text="Volume", foreground=color_gray, background=color_light_gray, font=("Helvetica", 16, "bold"))
volume_scale = tk.Scale(root, from_=0, to=100, orient='horizontal', command=set_volume,
                        foreground=color_gray, background=color_light_gray,
                        length=300, font=("Helvetica", 12))

# Display song title in the GUI
song_title = tk.StringVar()
song_label = tk.Label(root, textvariable=song_title, font=("Helvetica", 16, "bold"),background=color_blue)

# Arrange elements in the window
song_label.pack()
load_button.pack()
play_button.pack()
pause_button.pack()
stop_button.pack()
volume_label.pack()
volume_scale.pack()

# Run the application
root.mainloop()
