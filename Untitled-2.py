import tkinter as tk
from tkinter import ttk

# Átváltási formulák
def convert_length(value, from_unit, to_unit):
    length_units = {'yard': 0.9144, 'mérföld': 1609.344, 'kilométer': 1000, 'méter': 1, 'milliméter': 0.001}
    value_in_yards = value * length_units[from_unit]
    return value_in_yards / length_units[to_unit]

def convert_mass(value, from_unit, to_unit):
    mass_units = {'font': 1, 'kilogramm': 2.20462, 'gramm': 0.00220462, 'tonna': 2204.62}
    value_in_pounds = value * mass_units[from_unit]
    return value_in_pounds / mass_units[to_unit]

def convert_time(value, from_unit, to_unit):
    time_units = {'mp': 1, 'perc': 60, 'óra': 3600, 'nap': 86400}
    value_in_seconds = value * time_units[from_unit]
    return value_in_seconds / time_units[to_unit]

# Az átváltás függvények egyesítéséhez:
def convert(value, from_unit, to_unit, conversion_type):
    value = float(value)
    if conversion_type == 'length':
        return convert_length(value, from_unit, to_unit)
    elif conversion_type == 'mass':
        return convert_mass(value, from_unit, to_unit)
    elif conversion_type == 'time':
        return convert_time(value, from_unit, to_unit)

# Az átváltó ablakok létrehozása
def open_converter_window(root, conversion_type, units_dict):
    window = tk.Toplevel(root)
    window.title(f"{conversion_type.capitalize()} Átváltó")
    
    # Beviteli mező
    tk.Label(window, text="Érték:").grid(row=0, column=0)
    value_entry = tk.Entry(window)
    value_entry.grid(row=0, column=1)
    
    # Legördülő listák a kezdő és cél mértékegységhez
    tk.Label(window, text="Miról:").grid(row=1, column=0)
    from_unit_combobox = ttk.Combobox(window, values=units_dict)
    from_unit_combobox.grid(row=1, column=1)
    from_unit_combobox.set(units_dict[0])  # alapértelmezett érték
    
    tk.Label(window, text="Mire:").grid(row=2, column=0)
    to_unit_combobox = ttk.Combobox(window, values=units_dict)
    to_unit_combobox.grid(row=2, column=1)
    to_unit_combobox.set(units_dict[1])  # alapértelmezett érték
    
    # Eredmény megjelenítése
    result_label = tk.Label(window, text="Eredmény: ")
    result_label.grid(row=3, column=0, columnspan=2)
    
    # Átváltás gomb
    def calculate():
        value = value_entry.get()
        from_unit = from_unit_combobox.get()
        to_unit = to_unit_combobox.get()
        if value:
            result = convert(value, from_unit, to_unit, conversion_type)
            result_label.config(text=f"Eredmény: {result:.4f} {to_unit}")
    
    tk.Button(window, text="Átvált", command=calculate).grid(row=4, column=0)
    tk.Button(window, text="Exit", command=window.destroy).grid(row=4, column=1)

# Főablak
def create_main_window():
    root = tk.Tk()
    root.title("Átváltó")
    
    tk.Label(root, text="Mértékegység-átváltó", font=("Arial", 16)).pack(pady=10)
    
    # Gombok az egyes típusokhoz
    tk.Button(root, text="Hossz", command=lambda: open_converter_window(root, 'length', ['yard', 'mérföld', 'kilométer', 'méter', 'milliméter'])).pack(pady=5)
    tk.Button(root, text="Tömeg", command=lambda: open_converter_window(root, 'mass', ['font', 'kilogramm', 'gramm', 'tonna'])).pack(pady=5)
    tk.Button(root, text="Idő", command=lambda: open_converter_window(root, 'time', ['mp', 'perc', 'óra', 'nap'])).pack(pady=5)
    
    # Kilépés gomb
    tk.Button(root, text="Exit", command=root.quit).pack(pady=20)
    
    root.mainloop()

# Fő program
if __name__ == "__main__":
    create_main_window()
