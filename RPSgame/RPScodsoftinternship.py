
# This is the Rock paper scissors game with GUI and desired o/p.
# A separate project is made with jupyter that shows a simple commandline o/p without use of functions.




import tkinter as tk
from PIL import Image, ImageTk
import random


# choices..
choices = ["rock", "paper", "scissors"]



user_score = 0
computer_score = 0
round_count = 0
history = []



# functions initiated...
def play_game(user_choice):
    global user_score, computer_score, round_count
    round_count += 1


# Generating random choice...
    computer_choice = random.choice(choices)



# Determining the victor...
    if user_choice == computer_choice:
        result = "It's a tie!"



# please don't change the spaces here... something is wrong with my code :( 
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win this round!"
        user_score += 1



    else:
        result = "Computer wins this round!"
        computer_score += 1




# Labels (Update wale)
    user_choice_label.config(text=f"Your choice: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Your score: {user_score}\nComputer's score: {computer_score}")



# Check if it's the 10th round of the game or not .... if 10 rounds then game over...
    if round_count == 10:
        round_count = 0
        end_game()




# Inlined loop (CAN BE UPDATED FURTHER)
def end_game():
    global user_score, computer_score


    # total scores..
    total_score_label.config(text=f"Total Scores\nYour score: {user_score}\nComputer's score: {computer_score}")


    # Determining the ultimate winner...
    if user_score > computer_score:
        winner_label.config(text="Congratulations! You are the ultimate winner!", fg='#4CAF50')  # Green color
        history.append(f"Game {len(history)+1}: You won")


    elif user_score < computer_score:
        winner_label.config(text="Computer is the ultimate winner!", fg='#FF6347')  # Coral color
        history.append(f"Game {len(history)+1}: Computer won")


    
    else:
        winner_label.config(text="It's a tie! No ultimate winner.", fg='#555555')  # Dim gray color
        history.append(f"Game {len(history)+1}: It's a tie")

    # Enabling the result's access to the history tab/panel....
    history_listbox.insert(tk.END, history[-1])

    user_score = 0
    computer_score = 0


# third loop
def restart_game():

    global user_score, computer_score, history

    user_score = 0
    computer_score = 0

    history_listbox.delete(0, tk.END)

    history = []

    user_choice_label.config(text="")

    computer_choice_label.config(text="")

    result_label.config(text="")
    score_label.config(text="")

    total_score_label.config(text="")
    winner_label.config(text="")
    



# main window (GUI)
root = tk.Tk()
root.title("Welcome to Danish's RPS Game")
root.iconphoto(False, ImageTk.PhotoImage(Image.open("C:/Users/HP/AppData/Local/Programs/Python/Python310/RPSgame/icons/mainicon.png")))  #Game icon here...
root.configure(bg='#002838')  #background color here...




# Creating  a heading (idk if it's in the task or not but i'll put it just in case...)
heading_label = tk.Label(root, text="Welcome to Danish's RPS Game", font=("Helvetica", 18, "bold"), bg='#01161f', fg='#FFFFFF')
heading_label.pack(pady=10)



# Creating labels that will show scores...
user_choice_label = tk.Label(root, text="", font=("Helvetica", 14), bg='#01161f', fg='#FFFFFF')

computer_choice_label = tk.Label(root, text="", font=("Helvetica", 14), bg='#01161f', fg='#FFFFFF')

result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg='#01161f', fg='#FFFFFF')

score_label = tk.Label(root, text="", font=("Helvetica", 14), bg='#01161f', fg='#FFFFFF')

total_score_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg='#01161f', fg='#FFFFFF')

winner_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg='#01161f', fg='#FFFFFF')



# Creating buttons with icons for clicking (Click only buttons and not the labels)
button_icons = [

    ("rock", "C:/Users/HP/AppData/Local/Programs/Python/Python310/RPSgame/icons/rock.png"),
    ("paper", "C:/Users/HP/AppData/Local/Programs/Python/Python310/RPSgame/icons/paper.png"),
    ("scissors", "C:/Users/HP/AppData/Local/Programs/Python/Python310/RPSgame/icons/scissor.png")

]



# Setting icons and buttons...
for choice, icon_path in button_icons:
    icon = Image.open(icon_path)
    icon = icon.resize((50, 50), Image.ANTIALIAS)
    icon = ImageTk.PhotoImage(icon)


    button_frame = tk.Frame(root, bg='#01161f', bd=2, relief=tk.GROOVE)
    button_frame.pack(pady=5)
    
    
    button = tk.Button(button_frame, image=icon, command=lambda c=choice: play_game(c), bd=0, bg='#555555')
    button.image = icon
    button.pack(side=tk.LEFT, padx=5)


    label = tk.Label(button_frame, text=choice.capitalize(), font=("Helvetica", 12, "bold"), bg='#01161f', fg='#FFFFFF')
    label.pack(side=tk.LEFT, padx=5)


# Lamba sa text...
description_label = tk.Label(root, text="This game continues until 10 rounds. The one to score most scores shall be declared winner", font=("Helvetica", 12), bg='#01161f', fg='#FFFFFF')
description_label.pack(pady=10)



# History panel
history_frame = tk.Frame(root, bg='#020c24', bd=2, relief=tk.GROOVE)
history_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

history_label = tk.Label(history_frame, text="History", font=("Helvetica", 14, "bold"), bg='#020c24', fg='#FFFFFF')
history_label.pack(pady=5)

history_listbox = tk.Listbox(history_frame, width=30, height=10, font=("Helvetica", 12), bd=5, relief=tk.GROOVE, bg='#360500', fg='#FFFFFF')
history_listbox.pack(padx=10, pady=10)



# Restart button (Don't touch anything here... It's unstable...)
restart_button = tk.Button(root, text="Restart Game", command=lambda: restart_game(), bg='#4CAF50', fg='#020c24', font=("Helvetica", 12, "bold"))
restart_button.pack(pady=10)



# Packing the labels finally....
user_choice_label.pack(pady=10)
computer_choice_label.pack(pady=10)
result_label.pack(pady=10)
score_label.pack(pady=10)
total_score_label.pack(pady=10)
winner_label.pack(pady=10)



# Running the main loop
root.mainloop()
