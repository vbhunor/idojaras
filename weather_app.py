import threading
import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import io


API_KEY = "1b674e648abac0f8546ed6824e2e2fd3"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city, units):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": units,
            "lang": "hu"
        }
        # Proxy-t használva (munkahelyi hálózathoz)
        response = requests.get(
            BASE_URL,
            params=params,
            proxies={"https": "http://hubudae-proxy001.emea.nsn-net.net:8080"}
        )
        data = response.json()

        if response.status_code == 200:
            city_name = data["name"]
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            fok = "°C" if units == "metric" else "°F"
            result = f"Város: {city_name}\nHőmérséklet: {temp} {fok}\nIdőjárás: {weather.capitalize()}"
        else:
            result = f"Hiba: {data.get('message', 'Ismeretlen hiba')}"
    except Exception as e:
        result = f"Hiba történt: {e}"

    # Eredmény visszaadása a fő szálon
    result_label.after(0, lambda: result_label.config(text=result))


def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Adj meg egy városnevet!")
        return

    units = "metric" if unit_var.get() == "C" else "imperial"
    result_label.config(text="Lekérdezés folyamatban...")
    threading.Thread(target=get_weather_data, args=(city, units), daemon=True).start()


# GUI létrehozása
root = tk.Tk()
root.title("Időjárás lekérdező")

frame = ttk.Frame(root, padding=20)
frame.grid()
icon_label = ttk.Label(frame)
icon_label.grid(column=0, row=4, columnspan=2, pady=10)


# Város 
ttk.Label(frame, text="Város neve:").grid(column=0, row=0, sticky="W")
city_entry = ttk.Entry(frame, width=30)
city_entry.grid(column=1, row=0, padx=10)

# Celsius/Fahrenheit választási lehetőség
unit_var = tk.StringVar(value="C")
c_radio = ttk.Radiobutton(frame, text="Celsius", variable=unit_var, value="C")
f_radio = ttk.Radiobutton(frame, text="Fahrenheit", variable=unit_var, value="F")
c_radio.grid(column=0, row=1, sticky="W", pady=5)
f_radio.grid(column=1, row=1, sticky="W", pady=5)

# Gomb
get_weather_btn = ttk.Button(frame, text="Időjárás lekérdezése", command=get_weather)
get_weather_btn.grid(column=0, row=2, columnspan=2, pady=10)

# Eredmény
result_label = ttk.Label(frame, text="", justify="left")
result_label.grid(column=0, row=3, columnspan=2)

root.mainloop()
