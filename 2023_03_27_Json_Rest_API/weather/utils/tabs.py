import tkinter as tk
from tkinter import ttk


class WeatherTab(ttk.Frame):
    def __init__(self, parent: ttk.Notebook, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.self_curr = None
        self.self_desc_curr = None

        self.configure(height=200, width=326)
        self.columnconfigure(index=0, weight=1, minsize=200)
        self.columnconfigure(index=1, weight=1, minsize=126)
        # The rows that are not needed are just there to have a nice formatting
        self.rowconfigure(index=0, weight=1, minsize=33)
        self.rowconfigure(index=1, weight=1, minsize=33)
        self.rowconfigure(index=2, weight=1, minsize=33)
        self.rowconfigure(index=3, weight=1, minsize=33)
        self.rowconfigure(index=4, weight=1, minsize=34)
        self.rowconfigure(index=5, weight=1, minsize=34)

        self.setup_widgets()

        self.updatable = {"main": self.self_curr, "description": self.self_desc_curr}

    def setup_widgets(self):
        # Weather
        self_text = ttk.Label(self, text="Current:")
        self_text.grid(row=0, column=0, sticky="nw")
        self.self_curr = ttk.Label(self, text="")
        self.self_curr.grid(row=0, column=1, sticky="ne")

        # Weather Description
        self_desc_text = ttk.Label(self, text="Description:")
        self_desc_text.grid(row=1, column=0, sticky="nw")
        self.self_desc_curr = ttk.Label(self, text="")
        self.self_desc_curr.grid(row=1, column=1, sticky="ne")


class TemperatureTab(ttk.Frame):
    def __init__(self, parent: ttk.Notebook, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent

        self.temp_curr = None
        self.fl_curr = None
        self.min_curr = None
        self.max_curr = None
        self.pressure_curr = None
        self.humidity_curr = None

        self.updatable = {}

        self.configure(height=200, width=326)
        self.columnconfigure(index=0, weight=1, minsize=200)
        self.columnconfigure(index=1, weight=1, minsize=116)
        self.columnconfigure(index=2, weight=1, minsize=10)
        self.rowconfigure(index=0, weight=1, minsize=33)
        self.rowconfigure(index=1, weight=1, minsize=33)
        self.rowconfigure(index=2, weight=1, minsize=33)
        self.rowconfigure(index=3, weight=1, minsize=33)
        self.rowconfigure(index=4, weight=1, minsize=34)
        self.rowconfigure(index=5, weight=1, minsize=34)

        self.setup_widgets()

    def setup_widgets(self):
        # Temperature
        temp_text = ttk.Label(self, text="Current:")
        temp_text.grid(row=0, column=0, sticky="nw")
        temp_unit = ttk.Label(self, text="°C")
        temp_unit.grid(row=0, column=2, sticky="ne")
        self.temp_curr = ttk.Label(self, text="")
        self.temp_curr.grid(row=0, column=1, sticky="ne")

        # Feels Like
        fl_text = ttk.Label(self, text="Feels Like:")
        fl_text.grid(row=1, column=0, sticky="nw")
        fl_unit = ttk.Label(self, text="°C")
        fl_unit.grid(row=1, column=2, sticky="ne")
        self.fl_curr = ttk.Label(self, text="")
        self.fl_curr.grid(row=1, column=1, sticky="ne")

        # Min
        min_text = ttk.Label(self, text="Min:")
        min_text.grid(row=2, column=0, sticky="nw")
        min_unit = ttk.Label(self, text="°C")
        min_unit.grid(row=2, column=2, sticky="ne")
        self.min_curr = ttk.Label(self, text="")
        self.min_curr.grid(row=2, column=1, sticky="ne")

        # Max
        max_text = ttk.Label(self, text="Max:")
        max_text.grid(row=3, column=0, sticky="nw")
        max_unit = ttk.Label(self, text="°C")
        max_unit.grid(row=3, column=2, sticky="ne")
        self.max_curr = ttk.Label(self, text="")
        self.max_curr.grid(row=3, column=1, sticky="ne")

        # Pressure
        pressure_text = ttk.Label(self, text="Pressure:")
        pressure_text.grid(row=4, column=0, sticky="nw")
        pressure_unit = ttk.Label(self, text="hPa")
        pressure_unit.grid(row=4, column=2, sticky="ne")
        self.pressure_curr = ttk.Label(self, text="")
        self.pressure_curr.grid(row=4, column=1, sticky="ne")

        # Humidity
        humidity_text = ttk.Label(self, text="Humidity:")
        humidity_text.grid(row=5, column=0, sticky="nw")
        humidity_unit = ttk.Label(self, text="%")
        humidity_unit.grid(row=5, column=2, sticky="ne")
        self.humidity_curr = ttk.Label(self, text="")
        self.humidity_curr.grid(row=5, column=1, sticky="ne")

        self.updatable = {"temp": self.temp_curr, "feels_like": self.fl_curr, "temp_min": self.min_curr,
                          "temp_max": self.max_curr, "pressure": self.pressure_curr, "humidity": self.humidity_curr}


class AdditionalTab(ttk.Frame):
    def __init__(self, parent: ttk.Notebook, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent

        self.visibility_curr = None
        self.clouds_curr = None
        self.sunrise_curr = None
        self.sunset_curr = None

        self.updatable = {}

        self.configure(height=200, width=326)
        self.columnconfigure(index=0, weight=1, minsize=200)
        self.columnconfigure(index=1, weight=1, minsize=116)
        self.columnconfigure(index=2, weight=1, minsize=10)
        self.rowconfigure(index=0, weight=1, minsize=33)
        self.rowconfigure(index=1, weight=1, minsize=33)
        self.rowconfigure(index=2, weight=1, minsize=33)
        self.rowconfigure(index=3, weight=1, minsize=33)
        self.rowconfigure(index=4, weight=1, minsize=34)
        self.rowconfigure(index=5, weight=1, minsize=34)

        self.setup_widgets()

    def setup_widgets(self):
        # Visibility
        visibility_text = ttk.Label(self, text="Visibility:")
        visibility_text.grid(row=0, column=0, sticky="nw")
        visibility_unit = ttk.Label(self, text="km")
        visibility_unit.grid(row=0, column=2, sticky="ne")
        self.visibility_curr = ttk.Label(self, text="")
        self.visibility_curr.grid(row=0, column=1, sticky="ne")

        # Clouds
        clouds_text = ttk.Label(self, text="Clouds:")
        clouds_text.grid(row=1, column=0, sticky="nw")
        clouds_unit = ttk.Label(self, text="%")
        clouds_unit.grid(row=1, column=2, sticky="ne")
        self.clouds_curr = ttk.Label(self, text="")
        self.clouds_curr.grid(row=1, column=1, sticky="ne")

        # Sunrise
        sunrise_text = ttk.Label(self, text="Sunrise:")
        sunrise_text.grid(row=2, column=0, sticky="nw")
        sunrise_unit = ttk.Label(self, text="")
        sunrise_unit.grid(row=2, column=2, sticky="ne")
        self.sunrise_curr = ttk.Label(self, text="")
        self.sunrise_curr.grid(row=2, column=1, sticky="ne")

        # Sunset
        sunset_text = ttk.Label(self, text="Sunset:")
        sunset_text.grid(row=3, column=0, sticky="nw")
        sunset_unit = ttk.Label(self, text="")
        sunset_unit.grid(row=3, column=2, sticky="ne")
        self.sunset_curr = ttk.Label(self, text="")
        self.sunset_curr.grid(row=3, column=1, sticky="ne")

        self.updatable = {"visibility": self.visibility_curr, "clouds": self.clouds_curr, "sunrise": self.sunrise_curr,
                          "sunset": self.sunset_curr}


class WindTab(ttk.Frame):
    def __init__(self, parent: ttk.Notebook, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent

        self.wind_speed_curr = None
        self.wind_deg_curr = None

        self.updatable = {}

        self.configure(height=200, width=326)
        self.columnconfigure(index=0, weight=1, minsize=200)
        self.columnconfigure(index=1, weight=1, minsize=116)
        self.columnconfigure(index=2, weight=1, minsize=10)
        self.rowconfigure(index=0, weight=1, minsize=33)
        self.rowconfigure(index=1, weight=1, minsize=33)
        self.rowconfigure(index=2, weight=1, minsize=33)
        self.rowconfigure(index=3, weight=1, minsize=33)
        self.rowconfigure(index=4, weight=1, minsize=34)
        self.rowconfigure(index=5, weight=1, minsize=34)

        self.setup_widgets()

    def setup_widgets(self):
        # Wind Speed
        wind_speed_text = ttk.Label(self, text="Wind Speed:")
        wind_speed_text.grid(row=0, column=0, sticky="nw")
        wind_speed_unit = ttk.Label(self, text="m/s")
        wind_speed_unit.grid(row=0, column=2, sticky="ne")
        self.wind_speed_curr = ttk.Label(self, text="")
        self.wind_speed_curr.grid(row=0, column=1, sticky="ne")

        # Wind Direction
        wind_deg_text = ttk.Label(self, text="Wind Direction:")
        wind_deg_text.grid(row=1, column=0, sticky="nw")
        wind_deg_unit = ttk.Label(self, text="°")
        wind_deg_unit.grid(row=1, column=2, sticky="ne")
        self.wind_deg_curr = ttk.Label(self, text="")
        self.wind_deg_curr.grid(row=1, column=1, sticky="ne")

        self.updatable = {"speed": self.wind_speed_curr, "deg": self.wind_deg_curr}
