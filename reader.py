"""
Imlementamos nuestra funcines de lectura
"""
import json

# Función para la lectura de JSON 
def read_json_file(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        json_dict = json.load(f)
        f.close()
    return json_dict
