import tkinter as tk
from tkinter import filedialog
import pygame
import random

presidential_list = ["s.png","h.png","pp.png","c.png","d.png",]
prez = random.choice(presidential_list)


def update_image():
    image_path = prez
    image = tk.PhotoImage(file=image_path)
    label.configure(image=image)
    label.image = image


def play_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        status_label.config(text="Status: Playing")
        paused = False
    else:
        if selected_file:
            pygame.mixer.music.load(selected_file)
            pygame.mixer.music.play()
            status_label.config(text="Status: Playing")
            paused = False
            update_play_time()  # Start updating play time
            update_total_time()  # Start updating total time
        else:
            status_label.config(text="Status: No file selected")


def pause_music():
    global paused
    pygame.mixer.music.pause()
    status_label.config(text="Status: Paused")
    paused = True


def stop_music():
    pygame.mixer.music.stop()
    status_label.config(text="Status: Stopped")
    play_time_label.config(text="Play Time: 00:00")  # Reset play time label


def set_volume(volume):
    pygame.mixer.music.set_volume(volume)


def choose_file():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    update_total_time()  # Update total time when a new file is selected


def change_volume(value):
    volume = float(value) / 100
    set_volume(volume)


def update_play_time():
    if pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos() // 1000  # Convert to seconds
        minutes = current_time // 60
        seconds = current_time % 60
        play_time_label.config(text=f"Play Time: {minutes:02}:{seconds:02}")
    root.after(1000, update_play_time)  # Schedule the function to run again after 1 second


def changer():
    global prez
    a = prez
    prez = random.choice(presidential_list)
    if prez == a:
        changer()
    else:
        update_image()  # Update the image after changing the president
        root.after(10000, changer)  # Schedule the changer function to be called again after 10 seconds


def update_total_time():
    a = ""
    global prez
    if selected_file:
        audio = pygame.mixer.Sound(selected_file)
        total_time = audio.get_length()  # Get the total length of the audio in seconds
        minutes = int(total_time // 60)
        seconds = int(total_time % 60)
        total_time_label.config(text=f"Total Time: {minutes:02}:{seconds:02}")


# Initialize pygame
pygame.mixer.init()

# Create the main window
root = tk.Tk()
root.geometry("700x700")
root.resizable(True, True)
root.title("MP3 Player")
image = tk.PhotoImage(file=prez)
label = tk.Label(root, image=image)
label.pack()

# Create buttons
select_button = tk.Button(root, text="Select Music", command=choose_file)
play_button = tk.Button(root, text="Play", command=play_music)
pause_button = tk.Button(root, text="Pause", command=pause_music)
stop_button = tk.Button(root, text="Stop", command=stop_music)

# Create a volume slider
volume_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=change_volume)
volume_slider.set(50)  # Set initial volume to 50%

# Create a status label
status_label = tk.Label(root, text="Status: Stopped")

# Create a play time label
play_time_label = tk.Label(root, text="Play Time: 00:00")

# Create a total time label
total_time_label = tk.Label(root, text="Total Time: 00:00")

# Position widgets
select_button.pack(pady=10)
play_button.pack(pady=5)
pause_button.pack(pady=5)
stop_button.pack(pady=5)
volume_slider.pack(pady=10)
status_label.pack(pady=5)
play_time_label.pack(pady=5)
total_time_label.pack(pady=5)

# Global variable to track if music is paused
paused = False

# Schedule the changer function to be called every 10 seconds
root.after(10000, changer)

# Start the GUI main loop
root.mainloop()
