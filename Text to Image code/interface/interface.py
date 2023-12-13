from tkinter import *
import os


# Designing window for registration

def Singup():
    global Singup_screen
    Singup_screen = Toplevel(main_screen)
    Singup_screen.title("Singup")
    Singup_screen.geometry("600x400")

    global username
    global password
    global firstname
    global listname
    global username_entry
    global password_entry
    global firstname_entry
    global listname_entry
    username = StringVar()
    password = StringVar()
    firstnam = StringVar()
    listname = StringVar()

    Label(Singup_screen, text="Please enter details below").pack()
    Label(Singup_screen, text="").pack()
    username_lable = Label(Singup_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(Singup_screen, textvariable=username)
    username_entry.pack()
    firstname_lable = Label(Singup_screen,text="Firstname *")
    firstname_lable.pack()
    firstname_entry = Entry(Singup_screen, textvariable=firstnam)
    firstname_entry.pack()
    listname_lable = Label(Singup_screen,text="Listname *")
    listname_lable.pack()
    listname_entry = Entry(Singup_screen, textvariable=listname)
    listname_entry.pack()
    password_lable = Label(Singup_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(Singup_screen, textvariable=password, show='*')
    password_entry.pack()
    v0 = IntVar()
    v0.set(1)
    r1 = Radiobutton(Singup_screen, text="male",width=5, height=1, variable=v0, value=1).pack()
    r2 = Radiobutton(Singup_screen, text="female",width=5, height=1, variable=v0, value=2).pack()
    Label(Singup_screen, text="").pack()
    Button(Singup_screen, text="Singup", width=10, height=1, command=Singup_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("600x400")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()



# Implementing event on register button

def Singup_user():

    username_info = username.get()
    password_info = password.get()


    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    firstname_entry.delete(0, END)
    listname_entry.delete(0, END)
    Label(Singup_screen, text="Singup Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    firstname_entry.delete(0, END)
    listname_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Text To Image Generation")
    login_success_screen.geometry("1000x800")
    imagebox = Label(login_success_screen, text="Your Image ")
    imagebox.pack()
    imagebox = Text(login_success_screen, width=80, height=20)
    imagebox.pack(pady=20)
    entertext = Label(login_success_screen, text="Enter Your Text * ")
    entertext.pack()
    entertext = Text(login_success_screen, width=60, height=7)
    entertext.pack(pady=20)
    Button(login_success_screen, text="Enter").pack()
    Button(login_success_screen, text="Save").pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("600x400")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("600x400")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1200x500")
    main_screen.title("Text To Image Generation (Account Login)")
    Label(text="Select Your Choice", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="5", width="100", command=login).pack()
    Label(text="").pack()
    Button(text="Singup", height="5", width="100", command=Singup).pack()


    main_screen.mainloop()


main_account_screen()