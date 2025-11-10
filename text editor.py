import tkinter as tk
from tkinter import filedialog,messagebox

def new_file():
    text.delete(1.0,tk.END)

#open file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path,'r') as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())

#write and save file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path,'w') as file:
            file.write(text.get(1.0,tk.END))
            messagebox.showinfo("Success","File saved successfully!")

window_object = tk.Tk()
window_object.title("Simple Text Editor")
window_object.geometry("800x600")

menu_object = tk.Menu(window_object)
window_object.config(menu=menu_object)

file_menu_object = tk.Menu(menu_object)

menu_object.add_cascade(label="File",menu=file_menu_object)
file_menu_object.add_command(label="New",command=new_file)
file_menu_object.add_command(label="Open",command=open_file)
file_menu_object.add_command(label="Save",command=save_file)
file_menu_object.add_separator()
file_menu_object.add_command(label="Exit",command=window_object.quit)

text = tk.Text(window_object,wrap=tk.WORD,font=("helvetica",12),fg="blue")
text.pack(expand=tk.YES,fill=tk.BOTH)

window_object.mainloop()

