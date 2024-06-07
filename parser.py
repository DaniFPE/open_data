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
