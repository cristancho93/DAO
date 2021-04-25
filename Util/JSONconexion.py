import json 

class JsonConexion():
    def __init__(self):
        self.conexion = json.load(open("sources/computador.json"))

    def get_conexion(self):
        # print(self.conexion)
        return json.load(open("sources/computador.json"))
