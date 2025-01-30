"""
Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja
väljastab tulemuse Fahrenheiti kraadides.
"""


def convert(temperature, unit):
    if unit.lower().startswith("c"):
        result = temperature * 1.8 + 32
        return result, "fahrenheit"
    elif unit.lower().startswith("f"):
        result = (temperature - 32) / 1.8
        return result, "celsius"
    return "võimatu", "teisendada"


if __name__ == '__main__':
    temperature = float(input("Temperatuur: "))
    unit = input("Konverteeritava temperatuuri ühik (c/f/k): ")
    result_temperature, result_unit = convert(temperature, unit)
    print(f"{temperature} {unit} on {result_temperature} {result_unit}")
