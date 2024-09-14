produkte = [
    {"name": "Laptop", "price": 900},
    {"name": "Maus", "price": 20},
    {"name": "Monitor", "price": 150},
    {"name": "Tastatur", "price": 45},
    {"name": "USB-Stick", "price": 15}
]

sortierte_produkte = sorted(produkte, key=lambda produkt: produkt['price'])
print(sortierte_produkte)

teure_produkte = list(filter(lambda produkt: produkt['price'] > 50, produkte))
print(teure_produkte)
