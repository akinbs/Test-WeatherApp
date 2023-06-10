import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from tkinter import  *
import tkinter as tk
from datetime import datetime
from PIL import Image,ImageTk
from tkinter import messagebox

screen = Tk()
screen.title("TestWeatherApp")
screen.geometry("700x400")
screen.resizable(False,False)
ApiKey = ""

def GetWeather():
    try:

        City = SearchText.get()
        Locator = Nominatim(user_agent="geoapiExercises")
        location = Locator.geocode(City)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        print(result)

        home = pytz.timezone(result)
        LocalTime = datetime.now(home)
        CurrentTime = LocalTime.strftime("%I :%M %p")
        clock.config(text= CurrentTime)
        name.config(text= "Current Weather")

        api = "https://api.openweathermap.org/data/2.5/weather?q"+City+"&appid="+ApiKey
        jsonData = requests.get(api).json()
        condition = jsonData["weather"][0]["main"]
        description = jsonData["weather"][0]["description"]
        temp = int(jsonData["main"]["temp"]-273.15)
        pressure = jsonData["main"]["pressure"]
        humidity = jsonData["main"]["humidity"]
        wind =jsonData["wind"]["speed"]


        T.config(text=(temp,"°"))
        C.config(text=(condition,"|","FEELS LİKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalıd Entry!")





SearchText =Entry(screen,justify="center", width=15,font=("Arial",20,"bold"),bg="#00A9EE", border=10, foreground="white",borderwidth=5)
SearchText.place(x=235,y=35)
SearchText.focus()

SearchIcon = Image.open("search-icon.png")
ResizeImg = SearchIcon.resize((30,30), Image.ANTIALIAS)
NewIcon = ImageTk.PhotoImage(ResizeImg)
SeacrchButton = Button(image=NewIcon,borderwidth=0,cursor="hand2",bg="#00A9EE",activebackground="#00A9EE",command=GetWeather)
SeacrchButton.place(x=430,y=42)

logo = Image.open("Icon.png")
ResizeLogo = logo.resize((160,160), Image.ANTIALIAS)
NewLogo = ImageTk.PhotoImage(ResizeLogo)
LogoLabel = Label(image=NewLogo)
LogoLabel.place(x=130,y=85)

BottomBox = Image.open("img.png")
ResizedBottomBox = BottomBox.resize((600,100),Image.ANTIALIAS)
NewBottomBox = ImageTk.PhotoImage(ResizedBottomBox)
BottomBoxLabel = Label(image= NewBottomBox)
BottomBoxLabel.place(x=50,y=300)

name = Label(screen,font=("Arial",10,"bold"))
name.place(x=30,y=100)
clock = Label(screen,font=("Arial",10,"bold"))
clock.place(x=30, y=130)




WindLabel = Label(screen,text="WIND",font=("Arial",10,"bold"),foreground="white",bg="#FFA38B")
WindLabel.place(x=65, y=310)

HumLabel = Label(screen,text="HUMIDITY",font=("Arial",10,"bold"),foreground="white",bg="#FFA38B")
HumLabel.place(x=200, y=310)

DesLabel = Label(screen,text="DESCRIPTION",font=("Arial",10,"bold"),foreground="white",bg="#FFA38B")
DesLabel.place(x=370, y=310)

PresLabel = Label(screen,text="PRESSURE",font=("Arial",10,"bold"),foreground="white",bg="#FFA38B")
PresLabel.place(x=560, y=310)



T = Label(font=("Arial",10,"bold"),foreground="yellow")
T.place(x=400,y=150)
C = Label(font=("Arial",10,"bold"),foreground="yellow")
C.place(x=400,y=250)

w = Label(text="...",font=("Arial",10,"bold"),foreground="white",background="#FFA38B")
w.place(x=75,y=350)

h = Label(text="...",font=("Arial",10,"bold"),foreground="white",background="#FFA38B")
h.place(x=220,y=350)

d = Label(text="...",font=("Arial",10,"bold"),foreground="white",background="#FFA38B")
d.place(x=400,y=350)

p = Label(text="...",font=("Arial",10,"bold"),foreground="white",background="#FFA38B")
p.place(x=590,y=350)

screen.mainloop()


