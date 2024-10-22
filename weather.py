from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def getWeather():
    city = textfield.get()

    try:
        # Geolocation code
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        
        if location is None:
            name.config(text="City not found!")
            clock.config(text="")
            return

        # Get timezone information using TimezoneFinder
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

    except Exception as e:
        name.config(text="Error retrieving data")
        clock.config(text="")
        print(e)  # Print or log the error for debugging purposes
        return  # Exit the function in case of an error

    try:
        # Weather API code
        api_key = "5446f8bfe33b4d69baead4ce2586459a"  # Replace with your actual OpenWeatherMap API key
        api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        # Fetch weather data 
        Json_data = requests.get(api).json()

        # Checking weather API response is valid or invalid
        if Json_data.get('cod') != 200:
            name.config(text="City weather not found!")
            return

        # Extract weather information
        condition = Json_data['weather'][0]['main']
        description = Json_data['weather'][0]['description']
        temp = Json_data['main']['temp']  # Already in Celsius due to 'units=metric'
        pressure = Json_data['main']['pressure']
        humidity = Json_data['main']['humidity']  # Corrected 'humidity' spelling
        wind = Json_data['wind']['speed']

        # labels with the weather information
        t.config(text=f"{temp}°C")
        c.config(text=f"{condition} | FEELS LIKE {temp}°C")
        w.config(text=f"{wind}m/s")
        h.config(text=f"{humidity}%")
        d.config(text=f"{description.title()}")
        p.config(text=f"{pressure}hPa")

    except Exception as e:
        name.config(text="Error retrieving weather data")
        print(e)  # Print or log the error 



root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)


# Search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)


textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()


Search_icon = PhotoImage(file="search_icon.png")  
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040",command=getWeather)
myimage_icon.place(x=400, y=34)


#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#Bottom Box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("helvetica",20))
clock.place(x=30,y=130)


#Label
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=225,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)



t=Label(font=("arial",20,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)


w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)







root.mainloop()
