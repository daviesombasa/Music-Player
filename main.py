import tkinter.messagebox
from tkinter import ttk
from ttkthemes import themed_tk as tk


from backup_show import *

root = tk.ThemedTk()
root.get_themes()
root.set_theme("clearlooks")

mixer.init()  # Mixer initialization
root.title('Ombasa')
root.iconbitmap(r'images/vlc_icon.ico')

# Creating music background

back_image = PhotoImage(file='images/spin.png')
background = Label(root, image=back_image)
background.place(relwidth=1, relheight=1)

# Creating status bar
statusbar = ttk.Label(root, text='Welcome to Ombasa', relief=SUNKEN, anchor=W, font='Times 8 bold')
statusbar.pack(side=BOTTOM, fill=X)

# Creating function files


# Creating menu
menubar = Menu(root)
root.config(menu=menubar)

# Creating submenus
file_menu = Menu(menubar, tearoff=0)
help_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='File', menu=file_menu)
menubar.add_cascade(label='Help', menu=help_menu)

file_menu.add_command(label='New', command=file_browse)
file_menu.add_command(label='Exit', command=root.destroy)
help_menu.add_command(label='About Us', command=about_us)
help_menu.add_command(label='Exit', command=root.destroy)

# Creating frames
leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=25)

rightframe = Frame(root)
rightframe.pack()

topframe = Frame(rightframe)
topframe.pack()

midframe = Frame(rightframe)
midframe.pack(pady=10)

bottomframe = Frame(rightframe)
bottomframe.pack(pady=10)

# Create music text
length_label = ttk.Label(topframe, text='Total Length : --:--')
length_label.pack(pady=5)

current_label = ttk.Label(topframe, text='Current Time : --:--', relief=GROOVE)
current_label.pack()

# Creating Music List Box

play_music_list = Listbox(leftframe)
play_music_list.pack()

# Creating buttons
playPhoto = PhotoImage(file='images/play.png')
playButton = ttk.Button(midframe, image=playPhoto, command=play_music)
playButton.grid(row=0, padx=5)

stopPhoto = PhotoImage(file='images/stop-button.png')
stopButton = ttk.Button(midframe, image=stopPhoto, command=stop_music)
stopButton.grid(row=0, column=1, padx=5)

pausePhoto = PhotoImage(file='images/pause-button.png')
pauseButton = ttk.Button(midframe, image=pausePhoto, command=pause_music)
pauseButton.grid(row=0, column=2, padx=5)

rewindPhoto = PhotoImage(file='images/rewind.png')
rewindButton = ttk.Button(bottomframe, image=rewindPhoto, command=rewind_music)
rewindButton.grid(row=0, column=2, padx=5)

mutePhoto = PhotoImage(file='images/mute.png')
volumePhoto = PhotoImage(file='images/volume.png')
volumeButton = ttk.Button(bottomframe, image=volumePhoto, command=mute_music)
volumeButton.grid(row=0, column=0, padx=5)

add_music_photo = PhotoImage(file='images/add.png')
add_music_button = ttk.Button(leftframe, image=add_music_photo, command=file_browse)
add_music_button.pack(side=LEFT, pady=5)

del_music_photo = PhotoImage(file='images/remove.png')
del_music_button = ttk.Button(leftframe, image=del_music_photo, command=del_music)
del_music_button.pack(side=LEFT, padx=1, pady=5)

# Setting volume modifyer

scale = ttk.Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(40)
mixer.music.set_volume(0.4)
scale.grid(row=0, column=3)


def on_closing():
    tkinter.messagebox.showwarning('Close Music Player', 'Do you want to exit?')
    stop_music()
    root.destroy()


root.protocol('WM_DELETE_WINDOW', on_closing)
root.mainloop()
