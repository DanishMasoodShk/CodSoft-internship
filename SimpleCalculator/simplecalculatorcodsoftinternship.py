
#This is the GUI including Simple calculator with a little spice of my own.



import tkinter as tk

def on_button_click(value):
    current_text = entry.get()

    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))



def clear_entry():
    entry.delete(0, tk.END)



def calculate():
    try:
        result = eval(entry.get())
        current_text = entry.get()

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))

        history_listbox.insert(tk.END, f"{current_text} = {result}")


    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")




# Creating the main calculator window here...
root = tk.Tk()
root.title(" Calculator :3 ")

root.iconphoto(False, tk.PhotoImage(file="C:/Users/HP/AppData/Local/Programs/Python/Python310/SimpleCalculator/Cal_icon.png"))  # Main icon
root.configure(bg='#333333')  #Main bg




# Heading or label for the calculator ..
heading_label = tk.Label(root, text="MY CALCULATOR", font=("Goergia", 24, 'bold'), bg='#393b40', fg='#FFFFFF')
heading_label.grid(row=0, column=0, columnspan=4, pady=10)




# Creating bordered frame for the entry widget..
entry_frame = tk.LabelFrame(root, text="Calculations", font=("Helvetica", 14, 'bold'), bg='#333333', fg='#FFFFFF', bd=2, relief=tk.GROOVE)
entry_frame.grid(row=1, column=0, columnspan=4, pady=10)



#tk entery framing ..
entry = tk.Entry(entry_frame, width=16, font=("Helvetica", 20), bd=5, justify=tk.RIGHT, bg='#000e24', fg='#FFFFFF')
entry.grid(row=0, column=0, columnspan=4, pady=10)



# Label for the history tab   ..... Idk if it is essential or not.. nvm I'll just hide it for now..
#history_label = tk.Label(root, text="", font=("Helvetica", 16, 'bold'), bg='#333333', fg='#FFFFFF')
#history_label.grid(row=2, column=0, columnspan=4, pady=5)



# Creating bordered frame for the history listbox...
history_frame = tk.LabelFrame(root, text="History", font=("Helvetica", 14, 'bold'), bg='#393b40', fg='#FFFFFF', bd=1, relief=tk.GROOVE)
history_frame.grid(row=3, column=0, columnspan=4, pady=10)


history_listbox = tk.Listbox(history_frame, width=30, height=6, font=("Helvetica", 12), bd=5, relief=tk.GROOVE, bg='#000e24', fg='#FFFFFF')
history_listbox.pack(padx=10, pady=10)



# Defining the  button layout ... Please DON'T MOVE the ARRAY...
button_layout = [

    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3), #1

    ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3), #2

    ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3), #3

    ('0', 7, 0), ('C', 7, 1), ('=', 7, 2), ('+', 7, 3), #4

]

# Creating buttons and making space for them ... also placing them... 
for (text, row, col) in button_layout:
    if text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, command=clear_entry, bg='#FF6347', fg='#FFFFFF')  


    elif text == '=':
        button = tk.Button(root, text=text, width=5, height=2, command=calculate, bg='#4CAF50', fg='#FFFFFF')  


    else:
        button = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: on_button_click(t), bg='#555555', fg='#FFFFFF')


    button.grid(row=row, column=col, padx=5, pady=5)



# Binding keys .... this will make it easier... to operate..
root.bind('<Return>', lambda event: calculate())
root.bind('<Escape>', lambda event: clear_entry())



# Ending the main loop
root.mainloop()
