from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S26", "+79562541212"),
    Smartphone("Xiaomi", "Civi 5 Pro", "+79234561232"),
    Smartphone("Honor", "600 Pro", "+79524861532"),
    Smartphone("HUAWEI", "Pura 90 Pro Max", "+75624264562"),
    Smartphone("Realme", "P4 Power", "+79134521526")
]


for smartphone in catalog:
    print(f"{smartphone.phone}, {smartphone.model}, {smartphone.number}")
