from tkinter import *
from PIL import ImageTk,Image

from Panel import Panel
from tkinter import messagebox
import tkinter.font as font




class Login:



    def funzione(self,testo):
        if testo == "ciao":
            messagebox.showerror("Error", "Credentials not valid, please retry.")

        if testo == "hola":
            #frame.grid_forget()
            Panel(self.frame2)
            self.frame2.grid(row=2, column=1)


    def __init__(self):

        self.root = Tk()
        self.root.title('Soccer Ratings')

        image = Image.open("soccer.png")
        # Resize the image using resize() method
        resize_image = image.resize((350, 100))
        self.img = ImageTk.PhotoImage(resize_image)
        self.label_img = Label(self.root, image=self.img)
        self.label_img.grid(row=0, column=0, columnspan=3)

        #global frame

        self.frame = LabelFrame(self.root, pady=100, padx=100)
        self.frame.grid(row=2, column=1)

        self.frame2 = LabelFrame(self.root, pady=100, padx=100)

        myFont = font.Font(family='Calibri', size=12)
        user_label = Label(self.frame, text="Username: ",font=myFont)
        pass_label = Label(self.frame, text="Password: ",font=myFont)
        space_label1 = Label(self.frame, text=" ")
        space_label2 = Label(self.frame, text=" ")
        user_entry = Entry(self.frame, width=17,font=myFont)
        pass_entry = Entry(self.frame,width=17,font=myFont, show='*')
        user_label.grid(row=2, column=1)
        user_entry.grid(row=2, column=2)
        space_label1.grid(row=3, column=1)
        pass_label.grid(row=4, column=1)
        pass_entry.grid(row=4, column=2)
        login_button = Button(self.frame, text="Login", padx=20, pady=7, bg="#4eb6b0", font=myFont, command=lambda: self.funzione(str(user_entry.get())))

        space_label2.grid(row=5, column=1)
        login_button.grid(row=6, column=2)

        space_label5 = Label(self.frame, text="\n" + "\n")
        space_label5.grid(row=7, column=1)

        user_label2 = Label(self.frame, text="Username: ",font=myFont)
        pass_label2 = Label(self.frame, text="Password: ", font=myFont)
        space_label3 = Label(self.frame, text=" ")
        space_label4 = Label(self.frame, text=" ")
        user_entry2 = Entry(self.frame, width=17,font=myFont)
        pass_entry2 = Entry(self.frame, width=17,font=myFont)
        user_label2.grid(row=8, column=1)
        user_entry2.grid(row=8, column=2)
        space_label3.grid(row=9, column=1)
        pass_label2.grid(row=10, column=1)
        pass_entry2.grid(row=10, column=2)
        login_button2 = Button(self.frame, text="Register", padx=20, pady=7, bg="#1d434e", fg="white",font=myFont)
        space_label4.grid(row=11, column=1)
        login_button2.grid(row=12, column=2)

        space_label6 = Label(self.frame, text="                                             ")
        # space_label6.grid(row=1,column=4)

        space_label13 = Label(self.frame, text="\n" + "\n")



    def start(self):
        self.root.mainloop()


