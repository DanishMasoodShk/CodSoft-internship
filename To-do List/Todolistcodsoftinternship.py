#This project involved a GUI including To-Do List that can had user ADD , UPDATE and DELETE it's entries on a simple User Interface and userfriendnly mechanism.
#A separate file of py is made for command line o/p withiut use of any complicated code in Jupyter.


import tkinter as tk
from tkinter import*

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []
selected_index = None  #this is to keep track of the selected task index... oki?

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list, selected_index
    task_index = listbox.curselection()
    if task_index:
        task_index = int(task_index[0])
        task = listbox.get(task_index)
        if task in task_list:
            task_list.remove(task)
            with open("tasklist.txt", "w") as taskfile:
                for task in task_list:
                    taskfile.write(task + "\n")
            listbox.delete(task_index)
            selected_index = None

def updateTask(event):
    global task_list, selected_index
    if selected_index is not None:
        new_task = task_entry.get()
        if new_task:
            task_list[selected_index] = new_task
            with open("tasklist.txt", "w") as taskfile:
                for task in task_list:
                    taskfile.write(task + "\n")
            listbox.delete(selected_index)
            listbox.insert(selected_index, new_task)
            selected_index = None
            task_entry.delete(0, END)

def selectTask(event):
    global selected_index
    task_index = listbox.curselection()
    if task_index:
        selected_index = int(task_index[0])
        task = listbox.get(selected_index)
        task_entry.delete(0, END)
        task_entry.insert(0, task)

def openTaskFile():
    try:
        global task_list

        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open('tasklist.txt', 'w')
        file.close()

# Icon in the heading ....
Image_icon = PhotoImage(file="C:/Users/HP/AppData/Local/Programs/Python/Python310/To-do List/icons/task.png")
root.iconphoto(False, Image_icon)


# Top bar that gives the shade ... Wasn't able to give the proper dimension to stablize the color box ... so used image istead ... looks cool isn't it? ...
TopImage = PhotoImage(file="C:/Users/HP/AppData/Local/Programs/Python/Python310/To-do List/icons/topbar.png")
Label(root, image=TopImage).pack()


# Dock logo .... just to fill the top bar .... hehe
dockImage = PhotoImage(file="C:/Users/HP/AppData/Local/Programs/Python/Python310/To-do List/icons/dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)


# Note icon ... to show the authenticity it's required...
noteImage = PhotoImage(file="C:/Users/HP/AppData/Local/Programs/Python/Python310/To-do List/icons/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=310, y=25)

#Adding the heading ... here !
heading = Label(root, text="All Tasks", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# Main framework begins ... here !
frame = Frame(root, width=400, height=50, bg="#eddfbb")
frame.place(x=0, y=180)

#for it to have that textarea/textfeild section....

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()


#adding the ADD button here !

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#010212", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)



# Listbox ... scroll , TextArea for added entried to show up here....!!
frame1 = Frame(root, bd=3, width=700, height=200, bg="#010212")
frame1.pack(pady=(160, 0))


listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#261102", fg="white", cursor="hand2", selectbackground="#01052b")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

#Scrollbar works begins here...!!

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)


listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)



openTaskFile()



# Binding the updateTask function to the Enter key because adding Update key separately is a hassle.
root.bind('<Return>', updateTask)

# Binding  the selectTask function to the listbox selection event coz same reason.
listbox.bind('<ButtonRelease-1>', selectTask)

# Delete fucntions used here....
Delete_icon = PhotoImage(file="C:/Users/HP/AppData/Local/Programs/Python/Python310/To-do List/icons/delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)



#ending the loop...
root.mainloop()
