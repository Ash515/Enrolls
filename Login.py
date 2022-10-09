from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
import win32com.client as w
import random
import mysql.connector
from plyer import notification

root=Tk()

root.geometry("1540x900+0+0")
root.title("Login page")

# ==================adding Login Image here======================

bg_img1=Image.open("image/Login_background.png")
bg_img1=bg_img1.resize((1250,910),Image.ANTIALIAS)
photoimg1=ImageTk.PhotoImage(bg_img1)

f_Lable1=Label(root,image=photoimg1)
f_Lable1.place(x=350,y=0,width=1250,height=910)

#=========================== Main Frame ============================
main_Frame=Frame(f_Lable1,bg="white")
main_Frame.place(x=200,y=150,width=450,height=450)

#================================== Background image on Frame===================================

bg_img2=Image.open("image/Login.png")
bg_img2=bg_img2.resize((450,450),Image.ANTIALIAS)
photoimg=ImageTk.PhotoImage(bg_img2)

f_Lable=Label(main_Frame,image=photoimg)
f_Lable.place(x=0,y=0,width=450,height=450)


heading = Label(f_Lable,text="Login",font=("times new roman",25,"bold"),fg="Blue")
heading.place(x=185,y=20)

# ==========================created here username and password field==================================
username_label1 = Label(f_Lable,text="Username", font=("times new roman",15,"bold"))
username_label1.place(x=80,y=95)

password_label2 = Label(f_Lable,text="Password ", font=("times new roman",15,"bold"))
password_label2.place(x=80,y=150)

# ===========================entry for username and password============================
user_e1=Entry(f_Lable, font=["times new roman", 15])
user_e1.place(x=200,y=95,)

password_e2=Entry(f_Lable,font=("times new roman",15) , show="*", border=TRUE)
password_e2.place(x=200,y=150)


# =====================================Left Side image==================================

logo = Image.open("image/login_New.jpg")
logo = logo.resize((380, 450), Image.ANTIALIAS)
photoimg = ImageTk.PhotoImage(logo)

f_Lable2 = Label(root, image=photoimg)
f_Lable2.place(x=172, y=151, width=380, height=450)

def Register_Window():
    root.destroy()
    import Reg

def ForgotPassword_window():
    pass

# ==========================Captcha Automation==========================
text = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
captcha = StringVar()
input = StringVar()

def create_captcha():
    c = random.choices(text, k = 5)
    captcha.set(''.join(c))

# =============================Database creation and Captcha Automation=====================================
def check():
    username = user_e1.get()
    password = password_e2.get()
    if username == "" or password =="":
        messagebox.showerror("Error","All Fields Are Requirded",parent=root)
    else:
        try:
            # Add Your database details in here and create a backend also
            con = mysql.connector.connect(host="localhost", port=3306, user="root", password="", database="")

            cur = con.cursor()

            cur.execute("select * from reg where user='"+username+"'and password='"+password+"'")
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username And Password", parent=root)

            elif captcha.get() == input.get() :
                    messagebox.showinfo("Success", "Welcome To Quiz Guru", parent=root)
                    speak = w.Dispatch("SAPI.SpVoice")
                    speak.Speak("Welcome to Student Management Application")
                    title = "Student Management Application"
                    message = "Welcome to Student Management Application"
                    notification.notify(
                        title = title,
                        message = message,
                        app_icon = None,
                        timeout = 5,
                        toast = False
                    )
                    root.destroy()
                    import dashboard

            else:
                    messagebox.showerror('Captcha Verification', 'Incorrect Captcha')
            input.set('')
            create_captcha()

            con.close()

        except Exception as ae:
            messagebox.showerror("Error",f"Error due to ths str{ae}",parent=root)




Label(f_Lable,text="Captcha",font=("times new roman",16, "bold"),fg="Red").place(x=140,y=210)
Label(f_Lable, textvariable=captcha,text="Captcha",font=("times new roman",16, "bold")).place(x=140,y=240)
Entry(f_Lable, textvariable=input, bg='white', font="ariel 12 bold").place(x=140,y=280)

create_captcha()

# =====================================created button here like Login,sign up==================================
b1=Button(f_Lable,text="Login ",borderwidth=5,bg="blue",fg="white",font=("times new roman",12),padx=20, command=check)
b1.place(x=140,y=320)

b2=Button(f_Lable,text="Sign Up",command=Register_Window,borderwidth=5,bg="blue",fg="white",font=("times new roman",12),padx=20)
b2.place(x=250,y=320)

root.mainloop()
