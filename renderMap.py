from tkinter import *
from PIL import Image, ImageTk
from sys import argv

# MONITOR SETTINGS
# Get that information from this site: https://www.whatismyscreenresolution.org/
monitor_width = 1883
monitor_height = 934
monitor_width_inches = 19.6
monitor_height_inches = 9.7

# MAP SETTINGS
# Enter this information based on the map you are using
cells_per_row = 42
cells_per_column = 34

# Create window
root = Tk()
root.attributes("-fullscreen", True)

# Open the PDF file
image_path = argv[1]
img = Image.open(image_path)

original_width = img.width
original_height = img.height

scale_x = (monitor_width/  monitor_width_inches) / (original_width/ (cells_per_row))
scale_y = (monitor_height/ monitor_height_inches) / (original_height/ (cells_per_column))

new_size = (int(img.width * scale_x), int(img.height * scale_y))
img = img.resize(new_size, Image.Resampling.BICUBIC)

# Select the first page
photo = ImageTk.PhotoImage(img)

label = Label(root, image=photo)
label.pack()

def exit(event):
    root.destroy()

root.bind("<Escape>", exit)

root.mainloop()
