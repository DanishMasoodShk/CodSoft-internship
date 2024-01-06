#This is the contact book that includs GUI made in VScode
#A separate contact book is already made using python jupyter that shows command line o/p.
# I've not mentioned all the cmd comments here because my head is hurting bad.

import tkinter as tk
from tkinter import messagebox



class ContactBookApp:


    def __init__(self, root):


        self.root = root
        self.root.title("Danish's Contact Book")
        self.root.configure(bg='#010e2e')  


        # frame boundry... 
        self.frame = tk.Frame(root, bg='#d9d9d9', padx=10, pady=10)
        self.frame.grid(row=1, column=0, columnspan=2)

        self.contacts = []




        # LABELLLSSSSSSS... 
        tk.Label(self.frame, text="Name:", font=("Helvetica", 10, "bold"), bg='#010e2e', fg='#a6bdf7').grid(row=0, column=0, padx=10, pady=5, sticky="w")
       
        tk.Label(self.frame, text="Phone:", font=("Helvetica", 10, "bold"), bg='#010e2e', fg='#a6bdf7').grid(row=1, column=0, padx=10, pady=5, sticky="w")
       
        tk.Label(self.frame, text="Email:", font=("Helvetica", 10, "bold"), bg='#010e2e', fg='#a6bdf7').grid(row=2, column=0, padx=10, pady=5, sticky="w")
       
        tk.Label(self.frame, text="Address:", font=("Helvetica", 10, "bold"), bg='#010e2e', fg='#a6bdf7').grid(row=3, column=0, padx=10, pady=5, sticky="w")





        # Entry's spaces....
        self.name_entry = tk.Entry(self.frame, font=("Helvetica", 12), bg='#a6bdf7', fg='#010e2e')
        
        self.phone_entry = tk.Entry(self.frame, font=("Helvetica", 12), bg='#a6bdf7', fg='#010e2e')
        
        self.email_entry = tk.Entry(self.frame, font=("Helvetica", 12), bg='#a6bdf7', fg='#010e2e')
       
        self.address_entry = tk.Entry(self.frame, font=("Helvetica", 12), bg='#a6bdf7', fg='#010e2e')




        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
       
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)






        # Buttons with bold and colored text... DON"T TOUCH THIS ... IDK it's settled somehow..
        tk.Button(self.frame, text="Add Contact", command=self.add_contact, bg="#4CAF50", fg="#020c24", width=15, height=2, font=("Helvetica", 10, "bold")).grid(row=4, column=0, columnspan=2, pady=10)
        
        tk.Button(self.frame, text="View Contacts", command=self.view_contacts, bg="#3498db", fg="#020c24", width=15, height=2, font=("Helvetica", 10, "bold")).grid(row=5, column=0, columnspan=2, pady=10)
        
        tk.Button(self.frame, text="Search Contact", command=self.search_contact, bg="#e74c3c", fg="#020c24", width=15, height=2, font=("Helvetica", 10, "bold")).grid(row=6, column=0, columnspan=2, pady=10)
        
        tk.Button(self.frame, text="Update Contact", command=self.update_contact, bg="#f39c12", fg="#020c24", width=15, height=2, font=("Helvetica", 10, "bold")).grid(row=7, column=0, columnspan=2, pady=10)
        
        tk.Button(self.frame, text="Delete Contact", command=self.delete_contact, bg="#9b59b6", fg="#020c24", width=15, height=2, font=("Helvetica", 10, "bold")).grid(row=8, column=0, columnspan=2, pady=10)




        # Setting the icon in the taskbar... Please change the path in the system....
        self.root.iconphoto(False, tk.PhotoImage(file="C:/Users/HP/AppData/Local/Programs/Python/Python310/Contact Book/iconhaha.png"))





    def add_contact(self):

        name = self.name_entry.get()

        phone = self.phone_entry.get()

        email = self.email_entry.get()

        address = self.address_entry.get()




        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}

            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")


        else:
            messagebox.showerror("Error", "Name and Phone are required.")

        self.clear_entries()




    def view_contacts(self):
        if not self.contacts:

            messagebox.showinfo("No Contacts", "No contacts available.")

        else:
            contact_info = ""
            for contact in self.contacts:

                contact_info += f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n\n"
            
            messagebox.showinfo("Contact List", contact_info)



    def search_contact(self):
        name_to_search = self.name_entry.get()

        phone_to_search = self.phone_entry.get()

        if not name_to_search and not phone_to_search:


            messagebox.showerror("Error", "Enter Name or Phone to search.")
            return




        found_contacts = []
        for contact in self.contacts:

            if (name_to_search and name_to_search.lower() in contact["Name"].lower()) or \
               (phone_to_search and phone_to_search in contact["Phone"]):
                found_contacts.append(contact)





        if found_contacts:
            contact_info = ""
            for contact in found_contacts:

                contact_info += f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n\n"

            messagebox.showinfo("Search Result", contact_info)



        else:
            messagebox.showinfo("Search Result", "No matching contacts found.")





    def update_contact(self):
        name_to_update = self.name_entry.get()
        phone_to_update = self.phone_entry.get()




        if not name_to_update or not phone_to_update:
            messagebox.showerror("Error", "Enter Name and Phone to update.")
            return




        for contact in self.contacts:
            if contact["Name"] == name_to_update and contact["Phone"] == phone_to_update:
                contact["Email"] = self.email_entry.get()
                contact["Address"] = self.address_entry.get()

                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()

                return
        

        messagebox.showinfo("Not Found", "Contact not found for updating.")






    def delete_contact(self):
        name_to_delete = self.name_entry.get()
        phone_to_delete = self.phone_entry.get()



        if not name_to_delete or not phone_to_delete:
            messagebox.showerror("Error", "Enter Name and Phone to delete.")
            return



        for contact in self.contacts:
            if contact["Name"] == name_to_delete and contact["Phone"] == phone_to_delete:
                self.contacts.remove(contact)

                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.clear_entries()

                return


        messagebox.showinfo("Not Found", "Contact not found for deletion.")





    def clear_entries(self):
        self.name_entry.delete(0, tk.END)

        self.phone_entry.delete(0, tk.END)

        self.email_entry.delete(0, tk.END)

        self.address_entry.delete(0, tk.END)


        


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)


#Ending the main looop
    root.mainloop()
