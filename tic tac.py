from tkinter import *
from tkinter import messagebox

def check_winner():
    combo_list = [
        [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]
    ]

    for each_combo in combo_list:
        if buttons[each_combo[0]]["text"] == buttons[each_combo[1]]["text"] == buttons[each_combo[2]]["text"] !="":
            buttons[each_combo[0]].config(bg="green")
            buttons[each_combo[1]].config(bg="green")
            buttons[each_combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe",f"Player {buttons[each_combo[0]]['text']} wins!")
            root.quit()

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player} turn")

root = Tk()
root.title("Tic Tac Toe")

buttons = [
    Button(root,text="",font=("poppins",14),width=6,height=2,
    command=lambda i=i: button_click(i)) for i in range(9)
]

for i,button in enumerate(buttons):
    button.grid(row=i //3, column=i%3)

current_player = "X"
winner = False
label = Label(root,text=f"Player {current_player} turn",font=("poppins",14))
label.grid(row=3,column=0,columnspan=3)

root.mainloop()