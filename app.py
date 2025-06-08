from tkinter import *
import functioning
root = Tk()
root.title("Resume Builder")
root.geometry("900x650")
root.resizable(False, False)
root.config(bg="lightblue")


left_fields = [
    "Full Name", "Email", "Contact", "City",
    "Occupation", "Degree", "College", "CGPA","Interests","Branch","Current Year"
]

right_fields = [
    "Language (comma)", "Tools (comma seperate)", "Frameworks", "Project (comma seperate)","Tools/Tech Used",
    "Short description (Project)", "GitHub link (If Any)", "Intern (If Any)",
    "Certification", "Awards (If Any)",  "Experience"
]

entry_vars = {}

y_position = 60
for field in left_fields:
    Label(root, text=f"{field} :", bg="lightblue", anchor="w", font=("Arial", 10, "bold")).place(x=50, y=y_position)
    entry_var = StringVar()
    Entry(root, textvariable=entry_var, justify=CENTER, font=("Arial", 10)).place(x=140, y=y_position, width=250, height=25)
    entry_vars[field] = entry_var
    y_position += 40

y_position = 60
for field in right_fields:
    Label(root, text=f"{field} :", bg="lightblue", anchor="w", font=("Arial", 10, "bold")).place(x=420, y=y_position)
    entry_var = StringVar()
    Entry(root, textvariable=entry_var, justify=CENTER, font=("Arial", 10)).place(x=600, y=y_position, width=270, height=25)
    entry_vars[field] = entry_var
    y_position += 40

def print_data():
    keys = []
    values = []
    
    for key, var in entry_vars.items():
        keys.append(key)
        values.append(var.get())
        if(type(entry_var) == 'str') :
            entry_var.set("")  
        if(type(entry_var) == 'int') :
            entry_var.set(0)     
        if(type(entry_var) == 'float') :
            entry_var.set(0.0)  

    functioning.printList(keys,values)

    root.destroy()

        

Button(root, text="Get Resume ", command=print_data, bg="green", fg="white", font=("Arial", 10, "bold")).place(x=400, y=550)

root.mainloop()
