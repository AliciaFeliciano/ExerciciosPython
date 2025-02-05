def converter_temperatura(temperatura, unidade):
    if unidade == "C":
        fahrenheit = (temperatura * 9/5) + 32
        kelvin = temperatura + 273.15
    elif unidade == "F":
        celsius = (temperatura - 32) * 5/9
        kelvin = celsius + 273.15
    elif unidade == "K":
        celsius = temperatura - 273.15
        fahrenheit = (celsius * 9/5) + 32
    else:
        return "Unidade inválida. Use 'C', 'F' ou 'K'."

    return {
        "C": celsius if unidade != "C" else temperatura,
        "F": fahrenheit if unidade != "F" else temperatura,
        "K": kelvin if unidade != "K" else temperatura
    }