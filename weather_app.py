import tkinter as tk
from tkinter import font
import requests

H=500
W=500
#api.openweathermap.org/data/2.5/weather?q={city name},{country code}
#473dd79c63f11954431afcb82c510a6d
def print_entry(entry):
    print("this is entry : {}".format(entry))


def get_weather(city):
    weather_key = '473dd79c63f11954431afcb82c510a6d'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPId':weather_key,'q':city,'units':'Metric'}
    response = requests.get(url,params=params)
    weather_data =response.json()
    print(weather_data['name'])
    print(weather_data['weather'][0]['description'])
    print(weather_data['main']['temp_max'])
    print(weather_data['main']['temp_min'])
    label['text'] = f"City : {weather_data['name']} \n{weather_data['weather'][0]['description']} \nTemp : {weather_data['main']['temp_max']}"
window = tk.Tk()
window.title("My first project on Tkinter")

canvas =tk.Canvas(window,height=H,width=W)
canvas.pack()

frame =tk.Frame(window, bg="#5d9cec",bd=5,)
frame.place(relx=0.5,rely=0.1,relwidth=0.75, relheight=0.1,anchor="n") #anchor n=center

entry =tk.Entry(frame,bg="#ecf0f1",font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame,text= "Send",font=('Terminal',10) ,bg="white" , fg = "black", command = lambda: get_weather(entry.get()))
button.place(relx=0.7 ,relwidth=0.3, relheight = 1)

lower_frame=tk.Frame(window, bg = "#4392F1",bd=10)
lower_frame.place(relx=0.5,rely=0.25,relheight=0.6,relwidth=0.75,anchor="n")

label = tk.Label(lower_frame,font=('Montserrat',20),bg="white", anchor="nw",justify = 'left')
label.place(relwidth=1,relheight=1)


print(tk.font.families())

# print(entry)

window.mainloop()
