from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Soccer Ratings')

# Read the Image
image = Image.open("soccer.png")
# Resize the image using resize() method
resize_image = image.resize((300, 100))
img = ImageTk.PhotoImage(resize_image)
# Display the image
my_label = Label(image=img)
my_label.grid(row=0, column=0,columnspan=2)

#myButton = Button(root, text="Click me!",padx=25, pady=25,bg="#ffffff")
#myButton.grid(row=2, column=2)


user_label = Label(root, text="Username")
pass_label = Label(root, text="Password")
space_label1 = Label(root,text=" ")
space_label2 = Label(root,text=" ")
user_entry = Entry(root, width=25)
pass_entry = Entry(root, width=25)
user_label.grid(row=2,column=1)
user_entry.grid(row=2,column=2)
space_label1.grid(row=3,column=1)
pass_label.grid(row=4,column=1)
pass_entry.grid(row=4,column=2)
login_button = Button(root, text="Login",padx=25, pady=10,bg="#4eb6b0")
space_label2.grid(row=5,column=1)
login_button.grid(row=6, column=2)

space_label5 = Label(root,text="\n"+"\n")
space_label5.grid(row=7, column=1)

user_label2 = Label(root, text="Username")
pass_label2 = Label(root, text="Password")
space_label3 = Label(root,text=" ")
space_label4 = Label(root,text=" ")
user_entry2 = Entry(root, width=25)
pass_entry2 = Entry(root, width=25)
user_label2.grid(row=8,column=1)
user_entry2.grid(row=8,column=2)
space_label3.grid(row=9,column=1)
pass_label2.grid(row=10,column=1)
pass_entry2.grid(row=10,column=2)
login_button2 = Button(root, text="Register",padx=25, pady=10,bg="#1d434e", fg="white")
space_label4.grid(row=11,column=1)
login_button2.grid(row=12, column=2)

space_label6 = Label(root, text="                                             ")
space_label6.grid(row=1,column=4)

space_label13 = Label(root,text="\n"+"\n")
space_label13.grid(row=13, column=1)





root.mainloop()