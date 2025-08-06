import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your own API key
API_KEY = "your_openweathermap_api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

        return weather

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", f"City '{city}' not found!")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", str(e))

# Function to update the UI
def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    weather = get_weather(city)
    if weather:
        result_text = (
            f"City: {weather['city']}\n"
            f"Temperature: {weather['temperature']} °C\n"
            f"Humidity: {weather['humidity']} %\n"
            f"Description: {weather['description'].title()}\n"
            f"Wind Speed: {weather['wind_speed']} m/s"
        )
        result_label.config(text=result_text)

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Weather App", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12), command=show_weather)
search_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
