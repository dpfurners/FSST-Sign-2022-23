import tkinter as tk
from tkinter import ttk
from datetime import datetime, timezone

from .api import resolve_city_data, resolve_city_weather, get_weather_icon
from .tabs import WeatherTab, TemperatureTab, AdditionalTab, WindTab


def load_pre_searched_cities(file: str = "cities.wt") -> list[str]:
    try:
        with open(file, "r") as f:
            cities = f.read().splitlines()
            if len(cities) > 5:
                return cities[:5]
            return cities
    except FileNotFoundError:
        return []



def save_pre_searched_cities(cities: list[str], file: str = "cities.wt") -> None:
    with open(file, "w") as f:
        f.write("\n".join(cities))


def new_city(cb_city: ttk.Combobox, file: str = "cities.wt") -> None:
    city = cb_city.get()
    lang = resolve_city_data(city, lang=True)
    cities = load_pre_searched_cities(file)
    # Check if the city is already in the list (also different languages)
    for c in cities:
        if c == city:
            return
        if c in lang:
            return
    cities.insert(0, lang[0])
    cb_city["values"] = cities
    cb_city.option_clear()
    save_pre_searched_cities(cities, file)


def get_data(city: ttk.Combobox, labels: dict[dict, any], root: tk.Tk, file: str = "cities.wt") -> None:
    try:
        new_city(city, file)
        data = resolve_city_weather(city.get())
        for key, dic in data.items():
            if key in labels:
                if isinstance(dic, dict):
                    for key_d, value in dic.items():
                        if key_d in labels[key]:
                            if key_d in ["sunrise", "sunset"]:
                                value = datetime.fromtimestamp(value).strftime("%H:%M")
                            elif key_d == "visibility":
                                value = value/1000
                            labels[key][key_d].config(text=value)
                elif isinstance(dic, list):
                    dta = dic[0]
                    for key_d, value in dta.items():
                        if key_d in labels[key]:
                            if key_d == "icon":
                                icon = get_weather_icon(value)
                                photo = tk.PhotoImage(data=icon)
                                labels[key][key_d].config(image=photo)
                            else:
                                labels[key][key_d].config(text=value)
                else:
                    if key in data:
                        if key == "visibility":
                            dic = round(dic / 1000)
                        labels[key].config(text=dic)
        root.update()
    except:
        pass


def setup_widgets(root: tk.Tk) -> None:
    update_labels = {}

    root.resizable(False, False)
    root.columnconfigure(index=0, weight=1)
    root.columnconfigure(index=1, weight=1)
    root.columnconfigure(index=2, weight=1)
    root.rowconfigure(index=0, weight=1, minsize=30)
    root.rowconfigure(index=1, weight=1)
    root.rowconfigure(index=2, weight=1)

    city_inp = ttk.Combobox(root, width=30, values=load_pre_searched_cities())
    city_inp.grid(row=0, column=0, columnspan=2, sticky="nw")
    button = ttk.Button(root, text="Load_Data")
    button.grid(row=0, column=2, sticky="nw")

    # Notebook
    notebook = ttk.Notebook()
    notebook.grid(row=1, column=0, columnspan=3, rowspan=2, sticky="nw")

    # Weather Tab
    weather = WeatherTab(notebook)
    notebook.add(weather, text="Weather")
    update_labels["weather"] = weather.updatable

    # Temperature Tab
    temperature = TemperatureTab(notebook)
    notebook.add(temperature, text="Temperature")
    update_labels["main"] = temperature.updatable

    # Wind Tab
    wind = WindTab(notebook)
    notebook.add(wind, text="Wind")
    update_labels["wind"] = wind.updatable

    # Additional Tab
    additional = AdditionalTab(notebook)
    notebook.add(additional, text="Additional")
    update_labels["visibility"] = additional.updatable["visibility"]
    update_labels["clouds"] = {"all": additional.updatable["clouds"]}
    update_labels["sys"] = {"sunrise": additional.updatable["sunrise"], "sunset": additional.updatable["sunset"]}

    # Bind the button
    button.bind("<Button-1>", lambda event: get_data(city_inp, update_labels, root))


def initialize_tk(root: tk.Tk = None, theme: str | None = None) -> tuple[tk.Tk, ttk.Style | None]:
    if root is None:
        root = tk.Tk()
    root.title("Weather App")
    root.option_add("*tearOff", False)  # This is always a good idea

    # Center the window
    root.minsize(root.winfo_width(), root.winfo_height())
    x_coordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_coordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_coordinate, y_coordinate))

    # Create a style
    if theme is not None:
        style = ttk.Style(root)

        # Import the tcl file
        root.tk.call("source", "C:/_path/themes/tkinter/forest/forest-dark.tcl")

        # Set the theme with the theme_use method
        style.theme_use(theme)
        setup_widgets(root)
        return root, style
    setup_widgets(root)
    return root, None