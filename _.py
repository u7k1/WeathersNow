from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import base64
import time
import threading
from PIL import Image, ImageTk

def getWeather():
    city=textfield.get()

    geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
    location=geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    print('[*] '+result)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime('%I:%M %p')
        #Clock.config(text=current_time)
        # name.config(text='Current Time.')

    api_key = 'e01660d25700375d471a13a1115f88e4'  # Replace with your actual API key
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    json_data = requests.get(api_url).json()

    print('[*] Responed Code 200!')
    print(json_data)

    show_loading_screen(0.5)


    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,'°'))
        
    if temp > 30:
        def setLogo(image_path):
            # Logo_image = PhotoImage(file=image_path)
            # logo.config(image=Logo_image, width=195, height=195)
            # logo.image = Logo_image
            logo_image = Image.open(image_path)
            image_width = 195
            image_height = 195
        setLogo('sunny.png')
        t.config(fg='red')
        c.config(fg='red')
    else:
        
        Logo_image = PhotoImage(file='org_logo.png')
        logo.config(image=Logo_image)
        logo.image = Logo_image
        t.config(fg='blue')
        c.config(fg='blue')
        #root.update()
    root.update()

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)

def make_elements_invisible():
    for widget in root.winfo_children():
        if isinstance(widget, Label) or isinstance(widget, Button):
            widget.place_forget()
    myimage_icon.place_forget()
    frame_myimage.pack_forget()
    textfield.place_forget()

def make_elements_visible():
    myimage.place(x=20+int(search_box_y),y=20)
    textfield.place(x=50+int(search_box_y),y=40)
    myimage_icon.place(x=400+int(search_box_y),y=34)
    logo.place(x=150,y=100)
    frame_myimage.pack(padx=5, pady=5, side=BOTTOM)
    #name.place(x=30, y=100)
    #Clock.place(x=30,y=130)
    label1.place(x=120, y=400)
    label2.place(x=250, y=400)
    label3.place(x=430,y=400)
    label4.place (x=650,y=400)
    t.place (x=400, y=165)
    c.place(x=400,y=250)
    w.place(x=129,y=430)
    h.place(x=280,y=430)
    d.place(x=450,y=430)
    p.place(x=670,y=430)
    credit.place(x=745,y=0)

def show_loading_screen(sleep):
    # make_elements_invisible
    # background_label = Label(root, bg='black', width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    # background_label.place(x=0, y=0)

    # loading_label = Label(root, text="Please Wait....", compound="center", fg='Black', bg='white')  # Transparent background
    # loading_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # time.sleep(sleep)
    # background_label.destroy()
    # loading_label.destroy()
    # make_elements_visible()

    # make_elements_invisible()
    
    # background_label = Label(root, bg='grey')
    # background_label.place()#relwidth=1, relheight=1)
    # loading_label = Label(root, text="Please Wait....", compound="center", fg='Black')
    # loading_label.pack(anchor=CENTER)
    
    # time.sleep(sleep)

    # background_label.place_forget()
    # loading_label.pack_forget()
    # make_elements_visible()

    make_elements_invisible()
    
    background_label = Label(root, bg='black')
    background_label.place(relwidth=1, relheight=1)
    
    loading_label = Label(root, text="Please Wait....",font=('poppins',45,'bold'), compound="center", fg='White', bg='black')
    loading_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    root.update()  # Ensure the window updates
    
    time.sleep(2)  # Sleep for 2 seconds (simulating a loading operation)

    background_label.place_forget()
    loading_label.place_forget()
    make_elements_visible()



root=Tk()
root.title("Weather's Now")
root.geometry('900x500+300+200')
root.resizable(False, False)

search_box_y = 180

#
credit = Label(root, text='@u7k1: عثمان عوض الديحاني', bg='white', fg='black')
credit.place(x=745,y=0)
#search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image,)
myimage.place(x=20+int(search_box_y), y=20)
textfield=tk.Entry(root, justify="center",width=17,font=('poppins',25,'bold'),bg='black',border=0,fg='white')
textfield.place(x=50+int(search_box_y), y=40)
textfield.focus()

Search_icon=PhotoImage(file='search_icon.png')
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor='hand2',bg='black',command=getWeather)
myimage_icon.place(x=400+int(search_box_y), y=34)

#logo
Logo_image=PhotoImage(file="org_logo.png")
logo=Label(root, image=Logo_image, width=300, height=300)
logo.place(x=150,y=100)
#Bottom box
Frame_image=PhotoImage(file= "box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

#time
#name=Label(root,font=('arial', 15,'bold'))
#name.place(x=30, y=100)
#Clock=Label(root,font=('Helvetica',20))
#Clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica" ,15, 'bold'),fg="white" ,bg= "#111111")
label1.place(x=120, y=400)
label2=Label(root,text="HUMIDITY",font=("Helvetica" ,15, 'bold'),fg="white",bg="#111111")
label2.place(x=250, y=400)
label3=Label(root,text="DESCIPTION",font=("Helvetica" ,15, 'bold'),fg="white" ,bg="#111111")
label3.place (x=430,y=400)
label4=Label(root,text="PRESSURE",font=("Helvetica" ,15, 'bold'),fg="white" ,bg="#111111")
label4.place (x=650,y=400)

t=Label(font= ("arial" ,70, "bold"),fg="red")
t.place (x=400, y=165)
c=Label(font=('arial',15,'bold'),fg="red")
c.place(x=400,y=250)
w=Label(text="...",font=("arial" ,20, "bold"),fg="White" ,bg="#111111")
w.place(x=129,y=430)
h=Label(text="...",font=("arial" ,20, "bold"),fg="White" ,bg="#111111")
h.place(x=280,y=430)
d=Label(text="...",font=("arial" ,20, "bold"),fg="White" ,bg="#111111")
d.place(x=450,y=430)
p=Label(text="...",font=("arial" ,20, "bold"),fg="White" ,bg="#111111")
p.place(x=670,y=430)



root.mainloop()