# Python Program to Implement GOOGLE TRANSLATOR...

from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

root = Tk()
root.title('Google Translator Project')
root.geometry("740x400+200+100")
root.resizable(False,False)

def show():
    v1 = combo_first.get()
    v2 = combo_second.get()
    first_language.config(text=v1)
    second_language.config(text=v2)
    root.after(1000,show)

def translate():
    trans = Translator()
    trans_language = trans.translate(input_text.get(1.0,END),src=combo_first.get(),dest=combo_second.get())

    output_text.delete(1.0,END)
    output_text.insert(END,trans_language.text)

def clear():
    output_text.delete(1.0,END)
    input_text.delete(1.0,END)

def exit():
    root.destroy()

# we need to place icon image here...
image_icon = PhotoImage(file=r"E:\Google_translator\IMAGES\google.png")
root.iconphoto(False,image_icon)

bg_image = PhotoImage(file=r"E:\Google_translator\IMAGES\background.png")

lab = Label(root,image=bg_image)
lab.pack()

convert_image = PhotoImage(file=r"E:\Google_translator\IMAGES\Convert.png")
clear_image = PhotoImage(file=r"E:\Google_translator\IMAGES\clear.png")
exit_image = PhotoImage(file=r"E:\Google_translator\IMAGES\exit.png")

first_language = Label(root,text="English",font=("Engraves","30","bold"),fg = "#5582f9",bg = "white")
first_language.place(x = 90,y = 30)

second_language = Label(root,text="Telugu",font=("Engraves","30","bold"),bg = "#5582f9",fg = "white")
second_language.place(x = 500,y = 30)

language = list(LANGUAGES.values())

combo_first = ttk.Combobox(root,values = language)
combo_first.place(x = 90,y = 80)
combo_first.set('English')

combo_second = ttk.Combobox(root,values=language)
combo_second.place(x = 500,y = 80)
combo_second.set('Telugu')

input_text = Text(root,height=10,width=35,bg = "yellow",fg = "black")
input_text.place(x = 30,y = 100)

output_text = Text(root,height=10,width=35,fg = "black",bg = "white")
output_text.place(x = 430,y = 100)

convert = Button(root,text="convert",image=convert_image,bg="white",bd=0,command=translate)
convert.place(x = 43,y = 300)

clear = Button(root,text="clear",image=clear_image,bg = "#5582f9",bd=0,command=clear)
clear.place(x = 300,y = 300)

exit = Button(root,text="exit",image=exit_image,bg = "#5582f9",bd=0,command=exit)
exit.place(x = 530,y = 300)

show()

mainloop()