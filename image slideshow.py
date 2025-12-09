from itertools import cycle
from PIL import Image, ImageTk
import time
from tkinter import Tk, Label, Button
import os

def show_next_image():
    """
    Starts with the next image in the slideshow when the play button is clicked
    take 3 seconds to run
    """
    current_photo = next(slideshow)
    label.config(image=current_photo)
    window_object.after(3000,show_next_image)


def start_slideshow():
    show_next_image()

window_object = Tk()
window_object.title('Image Slideshow viewer')

# list of image path
image_path_list = [
    r"C:\Users\har4l\OneDrive\Pictures\Samsung Flow\20250422_120502.jpg",
    r"C:\Users\har4l\OneDrive\Pictures\Samsung Flow\20250731_132354.jpg",
    r"C:\Users\har4l\OneDrive\Pictures\Samsung Flow\20250803_093049.jpg",
    r"C:\Users\har4l\OneDrive\Pictures\Samsung Flow\20250803_093036.jpg",
    r"C:\Users\har4l\OneDrive\Pictures\Samsung Flow\20250803_093009.jpg",
    r"C:\Users\har4l\OneDrive\Pictures\Samsung Flow\4004174A-0E31-4B7C-97BF-976CE1DF0CF8L0001.jpg",
    r"C:\Users\har4l\OneDrive\Pictures\Samsung Flow\20250613_103735.jpg"
]

#list of paths that exists
existing_path_list = [each_path for each_path in image_path_list if os.path.exists(each_path)]

if not existing_path_list:
    print("Image not found at location, verify location")
    exit()

#resize image
resolution_size = (400,300)
image_list = [Image.open(each_path).resize(resolution_size) for each_path in existing_path_list]
photo_list = [ImageTk.PhotoImage(each_image) for each_image in image_list]

slideshow = cycle(photo_list)

#image label
label = Label(window_object)
label.pack(pady=10)

label.config(image=next(slideshow))
#to reset the slideshow after the first image
slideshow = cycle(photo_list)

play_button = Button(window_object, text="Play Slideshow", command=start_slideshow)
play_button.pack(pady=10)


window_object.mainloop()