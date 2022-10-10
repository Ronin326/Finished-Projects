from tkinter import *
from tkinter import filedialog
import pygame
import random
import time

#Inisialise
pygame.init()
pygame.mixer.init()

#TK Setup
window = Tk()
window.title("MUSIC PLAYER")
window.geometry("500x150")
window.configure(bg = 'black')

#Variables
global paused
global song_playing
global song_is_playing
display_name = StringVar()
paused          = False
song_is_playing = False
finish_song     = False
random_song = ''
song_playing = 0
display_x = 0
display_y = 10

#Played Lists
queue      = []
playlist   = []
song_names = []

#Song nameLabel
name = Label(window, textvariable = display_name,bg = "black",fg = "white",font=("Arial", 16))

#Functions
def add_songs():
    songs = filedialog.askopenfilenames(initialdir = 'C:/Users/ruanl/Music/', title = "Choose Song", filetypes = (("mp3 Files", "*.mp3"), ))
    for song in songs:
        queue.append(song)

def play_next():
    song = filedialog.askopenfilename(initialdir = 'C:/Users/ruanl/Music/All Music/', title = "Choose Song", filetypes = (("mp3 Files", "*.mp3"), ))
    if song not in playlist:
        playlist.append(song)
        song = song.replace("C:/Users/ruanl/Music/My Music/", "")
        song = song.replace(".mp3", "")
        song_names.append(song)
    else:
        pass

def play_time():
    current_time = pygame.mixer.music.get_pos()

#Button Functions
def play():
    global song_is_playing
    global finish_song
    global display_x
    display_x = 250
    if song_is_playing == False:
        global song_playing
        random_song = queue[random.randint(0, (len(queue)-1))]
        while random_song in playlist:
            random_song = queue[random.randint(0, len(queue)-1)]
        if random_song not in playlist:
            playlist.append(random_song)
            
            #Shorten Song Name
            random_song = random_song.replace("C:/Users/ruanl/Music/My Music/", "")
            random_song = random_song.replace(".mp3", "")
            song_names.append(random_song)
            
            song = playlist[song_playing]
        if len(playlist) == len(queue):
            song_playing = 0
            playlist.clear()

        display_name.set(song_names[song_playing])

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops = 0)
        song_is_playing = True
        finish_song = True

def stop():
    global song_is_playing
    global song_playing
    global finish_song
    display_name.set("")
    finish_song = False
    pygame.mixer.music.stop()
    playlist.clear()
    song_names.clear()
    song_playing = 0
    song_is_playing = False

def pause_play(is_paused):
    global paused
    global finish_song
    finish_song = False
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
        finish_song = True
    else:
        pygame.mixer.music.pause()
        paused = True

def next_song():
    global song_is_playing
    global song_playing
    global song
    global finish_song
    global display_x
    display_x = 250
    finish_song = False
    if song_is_playing:
        if song_playing > len(playlist)-2:
            random_song = queue[random.randint(0, len(queue)-1)]
            while random_song in playlist:
                random_song = queue[random.randint(0, len(queue)-1)]
            if random_song not in playlist:
                playlist.append(random_song)
            
                #Shorten Song Name
                random_song = random_song.replace("C:/Users/ruanl/Music/My Music/", "")
                random_song = random_song.replace(".mp3", "")
                song_names.append(random_song)
            
                song_playing += 1
                song = playlist[song_playing]
            if len(playlist) == len(queue):
                song_playing = 0
                playlist.clear()

            display_name.set(song_names[song_playing])
            
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops = 0)
            
        if song_playing < (len(playlist)-1):
            song_playing += 1
            song = playlist[song_playing]
            
            display_name.set(song_names[song_playing])

            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops = 0)
    finish_song = True

def previous_song():
    global song_playing
    global finish_song
    global display_x
    display_x = 250
    finish_song = False
    if song_playing == len(playlist):
        song_playing -= 1
    if len(playlist) > 1 and song_playing > 0:
        song_playing -= 1
        song = playlist[song_playing]
        
        display_name.set(song_names[song_playing])
        
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops = 0)
    finish_song = True

#Menu
my_menu = Menu(window)
my_menu.add_command(label = "Add Songs", command = add_songs)
my_menu.add_command(label = "Play Next", command = play_next)
window.config(menu = my_menu)

#Define Button Images
play_btn_img   = PhotoImage(file='C:/Users/ruanl/OneDrive/Pictures/Coding/Music App/play-button.png')
stop_btn_img   = PhotoImage(file='C:/Users/ruanl/OneDrive/Pictures/Coding/Music App/stop.png')
skip_btn_img   = PhotoImage(file='C:/Users/ruanl/OneDrive/Pictures/Coding/Music App/skip.png')
return_btn_img = PhotoImage(file='C:/Users/ruanl/OneDrive/Pictures/Coding/Music App/return.png')
pause_btn_img  = PhotoImage(file='C:/Users/ruanl/OneDrive/Pictures/Coding/Music App/play-pause.png')

#Button Frame
button_frame = Frame(window)
button_frame.pack(side = BOTTOM)

#Add Buttons
play_button   = Button(button_frame, image = play_btn_img  , borderwidth=0, command = play)
stop_button   = Button(button_frame, image = stop_btn_img  , borderwidth=0, command = stop)
skip_button   = Button(button_frame, image = skip_btn_img  , borderwidth=0, command = next_song)
return_button = Button(button_frame, image = return_btn_img, borderwidth=0, command = previous_song)
pause_button  = Button(button_frame, image = pause_btn_img , borderwidth=0, command = lambda: pause_play(paused))

#Grid Buttons
play_button.grid(row = 0, column = 1, padx = 19)
stop_button.grid(row = 0, column = 2, padx = 19)
skip_button.grid(row = 0, column = 4, padx = 19)
return_button.grid(row = 0, column = 3, padx = 19)
pause_button.grid(row = 0, column = 5, padx = 19)

while True:
    display_x -= 0.002
    name.place(x=display_x,y=display_y)
    window.update()
    if display_x < -600:
        display_x = 500
    if finish_song:
        if pygame.mixer.music.get_busy() == False:
            next_song()
    window.update()

window.mainloop()
