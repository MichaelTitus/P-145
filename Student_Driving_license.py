# Basic tkinter template

from tkinter import *

root = Tk();
root.title("Drivers License")
root.geometry("500x400")


root.configure(bg="Yellow")
canvas = Canvas(root, width=500, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 500, 55, fill="#1463B0")
canvas.create_rectangle(0, 345,500, 400, fill="#1463B0")

label_heading = canvas.create_text(150, 90, font=('Times', '24', 'bold italic'), text="Drivers License")
label_name_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="Name :")
label_date_tag = canvas.create_text(200, 205, font=('Times', '16', 'bold'), text="Date of Birth :")
label_place_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Address :")
label_car_tag = canvas.create_text(50, 300, font=('Times', '16', 'bold'), text="Car :")

label_name = Label(root)
label_date = Label(root)
label_place = Label(root)
label_car = Label(root)


def mycard():
    name = "Michael Titus"
    date = "May 19, 2010"
    place = "34487 tanguery dr."
    car = " The Driver can drive A land rover Discovery"
    
    label_name['text'] = name
    label_date['text'] = date
    label_date['text'] = place
    label_car['text'] = care


button1 = Button(root,text="show my Drivers License",command=mycard)

button1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_date_window = canvas.create_window(90, 205, anchor=CENTER, window=label_date)
label_place_window = canvas.create_window(240, 250, anchor=CENTER, window=label_place)
canvas.pack()

root.mainloop()
