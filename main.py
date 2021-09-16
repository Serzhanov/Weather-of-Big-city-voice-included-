import tkinter as tk
import time
import speech_recognition as sr
import sys
import requests
import os
import pyttsx3
import webbrowser
HEIGHT = 500
WIDTH = 600
def say():#function of reponsing
	r=sr.Recognizer()#the object of our library
	with sr.Microphone() as microe:
		say_that("now you can select the city")
		r.pause_threshold=1
		r.adjust_for_ambient_noise(microe,duration=1)#deleting outer noises
		a=r.listen(microe)#writing the city in variable
		try:
			new_a = r.recognize_google(a).lower()
			say_that(new_a)
		except:
			say_that("i can not hear you,say better")
			new_a=say()
		return new_a

def say_that(word):#fuction of speaking
	saying=pyttsx3.init()#initialisation of obiject of our library
	saying.say(word)
	time.sleep(1)
	saying.runAndWait()

def test_function(entry):
	print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
		say_that(final_str)
	except:
		final_str = 'There was a problem by retrieving that information'
		say_that("There was a problem by retrieving that information")
	return final_str

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()
	try:
		label['text'] = format_response(weather)
	except:
		say_that("it is  too")
def f():
	return get_weather(say())
say_that("Hello")

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
background_image = tk.PhotoImage(file='css.gif')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)
micro_image=tk.PhotoImage(file='l.png')
button = tk.Button(frame, text="Get Weather", font=('Courier',10), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.2)
button2=tk.Button(frame,command=lambda:f())
button2.place(relx=0.9,relheight=1,relwidth=0.1)
button2.config(image=micro_image)
lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
label = tk.Label(lower_frame,font=('Courier',12),anchor='nw',justify='left',bd=4)
label.place(relwidth=1, relheight=1)
root.mainloop()


