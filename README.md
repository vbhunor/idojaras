# idojaras



markdown
#  Időjárás Lekérdező Alkalmazás Dokumentáció

Ez a dokumentáció egy Pythonban írt, grafikus felhasználói felülettel (GUI) rendelkező időjárás-alkalmazást mutat be, amely az OpenWeatherMap API-t használja valós idejű időjárásadatok lekérdezésére. Az adatok megjelenítéséhez a `tkinter` könyvtárat alkalmazza, és a magyar nyelvű válaszokat kezeli.

---

##  Követelmények

Az alkalmazás működéséhez az alábbi csomagok szükségesek:

- `tkinter` – beépített GUI készítéséhez
- `threading` – aszinkron adatlekérdezés (GUI fagyásának elkerülése)
- `requests` – API-hívások küldéséhez
- `Pillow (PIL)` – képfeldolgozás (időjárás ikonhoz - opcionális)
- `io` – képadatok bájtfolyamként történő kezeléséhez

---

## API Beállítás

- **API Szolgáltató:** OpenWeatherMap
- **Alap URL:** `https://api.openweathermap.org/data/2.5/weather`
- **Autentikáció:** Egyéni API kulcs szükséges (`API_KEY`)
- **Proxy:** Munkahelyi hálózatok esetén használható:
  ```python
  proxies={"https": "http://hubudae-proxy001.emea.nsn-net.net:8080"}
Nyelv: Magyar ("lang": "hu")

Mértékegység: "metric" (°C) vagy "imperial" (°F)

🔧 Fő Funkciók
get_weather_data(city, units)
Ez a függvény végzi az időjárási adatok lekérdezését háttérszálon.

## Paraméterek:

city: A lekérdezendő város neve

units: "metric" vagy "imperial"

# Működés:

Lekéri az adatokat az API-tól

Feldolgozza a JSON választ

Hibakezelést alkalmaz

Eredményt frissít fő szálon: result_label.after()

get_weather()
A GUI gombhoz kapcsolódik:

Ellenőrzi, hogy a város mező üres-e

Meghatározza a kiválasztott mértékegységet

Elindítja az get_weather_data() függvényt új szálon

Visszajelzést ad a felhasználónak ("Lekérdezés folyamatban...")

Felhasználói Felület (GUI)
Komponens	Funkció
city_entry	Városnév bevitele
unit_var	Rádiógombok Celsius/Fahrenheit kiválasztához
get_weather_btn	Gomb az időjárás lekérdezéséhez
result_label	Eredmény megjelenítése szövegesen
icon_label	Előkészítve ikon megjelenítésére
A GUI a ttk.Frame segítségével épül fel, modern stílusban. A komponensek rácsba (grid) rendezve jelennek meg.

## Használat
Futtasd az alkalmazást:

bash
python weather_gui.py
Add meg a város nevét.

Válaszd ki a mértékegységet (Celsius vagy Fahrenheit).

Kattints az „Időjárás lekérdezése” gombra.

Pár másodpercen belül megjelenik az aktuális adat.

## Biztonsági Megjegyzések
Az API kulcsot javasolt biztonságosan kezelni (pl. .env fájlban tárolni).

A proxy csak munkahelyi környezetben szükséges.

Az alkalmazás nem fagy le, mivel a lekérdezés külön szálon történik.

