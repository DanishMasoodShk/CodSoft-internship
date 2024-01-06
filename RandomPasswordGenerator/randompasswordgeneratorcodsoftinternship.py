# This is Random Password Generator with GUI and few features. A separate project with command line o/p is made in juputer without using functions.


import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip


# Class creation for the Password Generator App...
class PasswordGeneratorApp:
    def __init__(self, root):

        self.root = root

        self.root.title("Dan's PASSWORD GENERATOR")

        self.root.configure(bg='#160236')  



 # Setting the app icon ...Change the paths if essential as per the system
        icon_path = "C:/Users/HP/AppData/Local/Programs/Python/Python310/RandomPasswordGenerator/Icons/icon.png"
        self.set_app_icon(icon_path)



 # Variables creations to store user input and generated password
        self.length_var = tk.StringVar(value="6") # Default: 6 ..

        self.include_upper_var = tk.BooleanVar(value=False)

        self.include_lower_var = tk.BooleanVar(value=True)  # Default: include lowercase characters..can be changed 

        self.include_digits_var = tk.BooleanVar(value=False)

        self.include_special_var = tk.BooleanVar(value=False)

        self.password_var = tk.StringVar()



# To store generated passwords...
        self.password_history = []  


 #To create the GUI components...
        self.create_widgets()


#please don't replace the functions or remove them ... It was a huge pain to fix them here... (took me 31 Minutes for just this to get fixxed)..
    def create_widgets(self):


        # Frames for password options..
        options_frame = tk.Frame(self.root, bg='#160236')
        options_frame.grid(row=0, column=0, padx=20, pady=20, sticky=tk.W)


        # For the Labels and Checkboxes for character options..
        length_label = tk.Label(options_frame, text="Password Length:", font=("Helvetica", 12, "bold"), bg='#160236', fg='#FFFFFF')
    
        length_label.grid(row=0, column=0, pady=10, sticky=tk.W)

        length_entry = tk.Entry(options_frame, textvariable=self.length_var, font=("Helvetica", 12), bd=5, justify=tk.CENTER, bg='#333333', fg='#FFFFFF', width=5)
       
        length_entry.grid(row=0, column=1, pady=10, padx=(0, 20), sticky=tk.W)



        #To create checkboxes with labels...
        self.create_checkbox(options_frame, "Uppercase", self.include_upper_var, 0, 0)

        self.create_checkbox(options_frame, "Lowercase", self.include_lower_var, 0, 1)

        self.create_checkbox(options_frame, "Digits", self.include_digits_var, 0, 2)

        self.create_checkbox(options_frame, "Special Characters", self.include_special_var, 0, 3)


        # To generate Password button here...
        generate_button = tk.Button(options_frame, text="Generate Password", command=self.generate_password, font=("Helvetica", 12, "bold"), bg='#4CAF50', fg='#FFFFFF')  
        generate_button.grid(row=2, column=0, columnspan=4, pady=(20, 10), sticky=tk.W)



        # Framing the generated password and copy button..
        result_frame = tk.Frame(self.root, bg='#160236')
        result_frame.grid(row=1, column=0, padx=20, pady=20, sticky=tk.W)



        # Displaying the  generated password..
        password_label = tk.Label(result_frame, text="Generated Password:", font=("Helvetica", 12, "bold"), bg='#160236', fg='#FFFFFF')
        password_label.grid(row=0, column=0, pady=(0, 10), sticky=tk.W)





#And this includes enteries....
        password_entry = tk.Entry(result_frame, textvariable=self.password_var, state='readonly', font=("Helvetica", 12), bd=5, justify=tk.CENTER, bg='#333333', fg='#13022e')
        password_entry.grid(row=1, column=0, pady=(0, 10), sticky=tk.W)


        # Button for the copy password to clipboard feature....
        copy_button = tk.Button(result_frame, text="Copy to Clipboard", command=self.copy_to_clipboard, font=("Helvetica", 12, "bold"), bg='#007BFF', fg='#FFFFFF')
        copy_button.grid(row=2, column=0, pady=(0, 10), sticky=tk.W)


        # Password history panel...
        history_frame = tk.Frame(self.root, bg='#160236')
        history_frame.grid(row=0, column=1, rowspan=2, padx=20, pady=20, sticky=tk.W)


        history_label = tk.Label(history_frame, text="Password History:", font=("Helvetica", 12, "bold"), bg='#160236', fg='#FFFFFF')
        history_label.grid(row=0, column=0, pady=(0, 10), sticky=tk.W)


        self.history_text = tk.Text(history_frame, height=10, width=25, font=("Helvetica", 10 , "bold"), bd=5, bg='#420121', fg='#FFFFFF')
        self.history_text.grid(row=1, column=0, pady=(0, 10), sticky=tk.W)


    # Needed to recreate the role module..
    def create_checkbox(self, parent, text, variable, row, column):

        # Function creation in order to create checkboxes with labels...
        checkbox = tk.Checkbutton(parent, text=text, variable=variable,  command=self.update_checkbox, font=("Helvetica", 12, "bold"), bg='#a564f5', fg='#2e0301')
        checkbox.grid(row=1, column=column, padx=(0, 20), sticky=tk.W)



    def update_checkbox(self):
        # This function is called when a checkbox is clicked... This was needed
        # It ensures that the checkbox stays checked until clicked again...
        pass


    def generate_password(self):

        try:
            length = int(self.length_var.get())
            if length <= 0:
                raise ValueError("Password length must be a positive integer. Pagal")
            


            characters = ""
            if self.include_upper_var.get():
                characters += string.ascii_uppercase


            if self.include_lower_var.get():
                characters += string.ascii_lowercase


            if self.include_digits_var.get():
                characters += string.digits


            if self.include_special_var.get():
                characters += string.punctuation


            if not characters:
                raise ValueError("Please select at least one type of characters.")
            



            # Generate password
            password = ''.join(random.choice(characters) for _ in range(length))

            # Display password
            self.password_var.set(password)

            # Add password to history
            self.password_history.append(password)
            self.update_history_text()


        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):

        password = self.password_var.get()
        if password:

            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard.")


        else:
            messagebox.showwarning("Warning", "Generate a password first.")




    def update_history_text(self):
        # Function to update the password history text..
        # Clear existing text....
        self.history_text.delete(1.0, tk.END)




        # Display password history
        for idx, password in enumerate(self.password_history, start=1):
            self.history_text.insert(tk.END, f"{idx}. {password}\n")




    def set_app_icon(self, icon_path):
        # Function to set the app icon.. 
        try:
            icon = tk.PhotoImage(file=icon_path)


            self.root.tk.call("wm", "iconphoto", self.root._w, icon)

        except Exception as e:
            print(f"Error setting app icon: {e}")



# Ending the loop FINALLY!

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.geometry("850x400") 
    root.mainloop()