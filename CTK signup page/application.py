from customtkinter import *
from PIL import Image
import random
import json




def SignUp():
    accounts = 'users.json'
    key_creation = random.randint(1, 100000)

    with open(accounts, 'r') as f:
        j = json.load(f)
        j[key_creation] = {"Full Name": first_last.get(), "Password": password.get(), "Email": email.get(), "ID": key_creation}
        with open(accounts, 'w') as b:
            json.dump(j, b, indent=4)
            print("successfully created account")





app = CTk()
app.geometry("800x700")

header =  CTkLabel(app, text='Sign Up', font=CTkFont("Arial", 40), text_color="#57008E")
header.pack(anchor='center', pady=10)

first_last = CTkEntry(master=app, placeholder_text='First and Last name', width=300, height=30)
first_last.pack(anchor='center', pady=10)

password = CTkEntry(master=app, placeholder_text='password',  width=300, height=30)
password.pack(anchor='center', pady=10)

email = CTkEntry(app, placeholder_text='Enter your email',  width=300, height=30)
email.pack(anchor='center', pady=10)

create  = CTkButton(app, text='Create Account', fg_color="#3F9535", hover_color='#3F9535', corner_radius=1000, command=SignUp)
create.pack(anchor='center', pady=10)


app.mainloop()