from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
def handle_login():
    email=email_Input.get()
    password=password_Input.get()
    # print(email,password)
    if email=='naman123@gmail.com' and password=='1234':
        messagebox.showinfo('Login Successful!')
    else:
        messagebox.showerror('Login Failed!')

root=Tk()
root.title('Login Window')
root.iconbitmap('icon.png')
# root.maxsize(400,400)
root.geometry('350x500')
root.config(background='#0096DC')
img=Image.open('logo.png')
resized_image=img.resize((100,100))
img=ImageTk.PhotoImage(resized_image)
img_label=Label(root,image=img)
img_label.pack(pady=(10,10))



text_label=Label(root,text='Sample Website',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

email_label=Label(root,text='Enter E-Mail',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',14))

email_Input=Entry(root, width=50)
email_Input.pack(ipady=6,pady=(1,15))
password_label=Label(root,text='Enter Password', fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',14))
password_Input=Entry(root,width=50)
password_Input.pack(ipady=6,pady=(1,15))
button=Button(root,text='Submit',bg='white',fg='black', width=20,height=2,command=handle_login)
button.pack(pady=(10,20))
button.config(font=('verdana',10))
root.mainloop()
