from customtkinter import *
from selenium import webdriver
import random
import json





def SignUp():
    accounts = 'users.json'
    key_creation = username.get()

    with open(accounts, 'r') as f:
        j = json.load(f)
        j[key_creation] = {"Username": username.get(), "Password": password.get(), "Email": email.get(), "ID": key_creation}
        with open(accounts, 'w') as b:
            json.dump(j, b, indent=4)
            print("successfully created account")


def login():
    accounts = 'users.json'
    gra = username_l.get()
    try:
     if gra:
         
      with open(accounts, 'r') as f:
            j = json.load(f)
            if gra == j[gra]["Username"]:          
                passW = pass_l.get()
                if passW == j[gra]["Password"]:
                    print("email: ", j[gra]["Email"]) #verifys email
                    print("successfully logged in")
                    
                    #application/code goes here
                    #---------------------
                    print("\nACTIONS/CMDS----\n1. account\n2. change password\n3. change email")
                    input1 = int(input("CHOICE: "))
                    if input1 == 1:
                        print(f'username: {gra}') #gets username
                        print(f'password: {passW}') #gets password
                        print(f'email: {j[gra]["Email"]}') #gets email
                        print(f'id: {j[gra]["ID"]}') #gets id
                    elif input1 == 2:
                        input2 = input("New password: ")
                        j[gra].update({"Password": input2}) #updates password to new input
                        with open(accounts, 'w') as r:
                            json.dump(j, r, indent=4) #saves file
                            print("changed password successfully")
                    elif input1 == 3:
                        input3 = input("New Email: ")
                        j[gra].update({"Email": input3}) #updates email to new input
                        with open(accounts, 'w') as b:
                            json.dump(j, b, indent=4) #saves file
                            print("successfully changed email")

                else:
                    print("worng password")

     else:
        print("no username inputed")
    except:
         print("username is incorrect")

      
        

       





app = CTk()
app.geometry("800x700")

header =  CTkLabel(app, text='Sign Up', font=CTkFont("Times New Roman Bold", 40), text_color="#57008E")
header.pack(anchor='center', pady=10)

username = CTkEntry(master=app, placeholder_text='Username', width=300, height=30)
username.pack(anchor='center', pady=10)

password = CTkEntry(master=app, placeholder_text='password',  width=300, height=30)
password.pack(anchor='center', pady=10)

email = CTkEntry(app, placeholder_text='Enter your email',  width=300, height=30)
email.pack(anchor='center', pady=10)

create  = CTkButton(app, text='Create Account', fg_color="#3F9535", hover_color='#3F9535', corner_radius=1000, command=SignUp)
create.pack(anchor='center', pady=10)

h2 = CTkLabel(app, text='Login', font=CTkFont("Times New Roman Bold", 40))
h2.pack(anchor='center', pady=10)

username_l = CTkEntry(app, placeholder_text='Username of account',  width=300, height=30)
username_l.pack(anchor='center', pady=10)

pass_l = CTkEntry(app, placeholder_text='Enter Password',  width=300, height=30)
pass_l.pack(anchor='center', pady=10)

l_login = CTkButton(app, text='Login', fg_color="#3F9535", hover_color='#3F9535', corner_radius=1000, command=login)
l_login.pack(anchor='center', pady=10)

app.mainloop()
