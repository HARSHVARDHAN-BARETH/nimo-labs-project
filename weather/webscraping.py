import requests
from bs4 import BeautifulSoup
from tkinter import *

def getWeather(city):
    url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        weather_data = soup.find('span', {'class': 'phrase'})
        return weather_data.text.strip()
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def onEntryClick(event):
    if entry.get() == "Enter city":
        entry.delete(0, END)
        entry.config(fg='black')

def changeWeather():
    city = entry.get()
    weather = getWeather(city)
    status.config(text=weather, fg="black")

root = Tk()
root.title("Weather Forecast")
root.resizable(0, 0)

windowWidth = 850
windowHeight = 400
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
xPositon = (screenWidth - windowWidth) // 2
yPosition = (screenHeight - windowHeight) // 2

root.geometry(f"{windowWidth}x{windowHeight}+{xPositon}+{yPosition}")
root.configure(bg='#e6f7ff')  

label = Label(root, text="Weather Forecast", bg='#e6f7ff', fg='#004080', font=('Helvetica', 45, 'bold'))
label.pack(pady=(30, 15))  

entry = Entry(root, width=30, bd=3, font=('Helvetica', 12), relief='solid', justify='center')  
entry.insert(10, "Enter city")
entry.config(fg='#808080', insertbackground='#808080')
entry.bind('<FocusIn>', onEntryClick)
entry.pack(pady=15)

button = Button(root, text='Get Weather', bg='#004080', fg='white', command=changeWeather,
                width=15, height=2, bd=3, font=('Helvetica', 12), relief='flat')
button.pack(pady=15)

status = Label(root, text="", bg='#e6f7ff', fg='#006600', font=('Helvetica', 12, 'italic'))
status.pack(pady=15)

root.mainloop()
