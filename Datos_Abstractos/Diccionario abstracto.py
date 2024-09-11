class Pareja:
    def __init__(self, llave, valor) -> None:
        self.llave_valor = (llave, valor)
        
class LlaveNoEncontrada(Exception):
    def __init__(self) -> None:
        mensaje: str = "La llave no fue encontrada en el diccionario"
        super().__init__(mensaje)
        
# implementacion basada en listas de python
class Diccionario:
    def __init__(self) -> None:
        self.datos = []
        
    def agregar_pareja(self, llave, valor):
        for pareja in self.datos:
            if llave == pareja[0]:
                return "Clave duplicada"
        self.datos.append((llave, valor))
        return "Pareja agregada"
    
    def modificar_pareja(self, llave, nuevo_valor):
        for idx, pareja in enumerate(self.datos):
            if llave == pareja[0]:
                self.datos[idx] = (llave, nuevo_valor)
                return "Llave modificada..."
        raise LlaveNoEncontrada
            


d = Diccionario()
d.agregar_pareja(4, 5)
d.agregar_pareja(5, 5)
d.agregar_pareja(6, 5)
d.agregar_pareja(7, 5)
d.agregar_pareja(8, 5)
d.modificar_pareja(10, 7)
print(d.datos)
