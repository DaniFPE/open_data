import matplotlib.pyplot as plt
import numpy as np

from reader import read_json_file


def parse_aire_dict(lista_aire_dict):
    """Esta función toma los datos originales y los parsea en un formato
    más sencillo de manejar para nuestros fines.

    Args:
        aire_dict (dict): Datos originales en formato dict.

    Returns:
        dict: Datos parseados.
    """
    data_por_estacion = dict()
    for data in lista_aire_dict:
        estacion = data["título"]
        fecha = data["fecha"]
        if estacion not in data_por_estacion:
            data_por_fecha = {fecha: {"pm25": [data["pm25"]],
                                    "hora": [data["periodo"]]}
                                    }
            data_por_estacion[estacion] = data_por_fecha
        else:
            if fecha not in data_por_estacion[estacion]:
                data_por_fecha = {fecha: {"pm25": [data["pm25"]],
                                    "hora": [data["periodo"]]}
                                    }
                data_por_estacion[estacion] = data_por_fecha
            else:
                data_por_estacion[estacion][fecha]["pm25"].append(data["pm25"])
                data_por_estacion[estacion][fecha]["hora"].append(data["periodo"])
    
    # Damos la vuelta a las listas
    for estacion in data_por_estacion:
        for fecha in data_por_estacion[estacion]:
            data = data_por_estacion[estacion][fecha]
            data["pm25"].reverse()
            data["hora"].reverse()

    return data_por_estacion

aire_dict = read_json_file("datos_aire.json")
lista_aire_dict = aire_dict["calidadairemediatemporales"]["calidadairemediatemporal"]

data_por_estacion = parse_aire_dict(lista_aire_dict)

# codigos_estacion_dict = {lista_data_aire for key in lista_data_aire}

# for n, estacion in enumerate(data_por_estacion):
#     print("Codigo: %s, Estación: %s" % (n, estacion))

# input("Selecciona estación:")

for estacion in data_por_estacion:
    data = data_por_estacion[estacion]["2024-04-19"]

    pm25 = data["pm25"]
    hora = data["hora"]
    

    plt.plot(hora, pm25)

hora_parsed = ["%2d:00" % hora for hora in hora]
plt.xticks(hora, hora_parsed, rotation=45)
plt.title("Pm25 al día")
plt.grid()
plt.axhline(y = 10, color = 'r', linestyle = 'dashed')  
plt.show()
