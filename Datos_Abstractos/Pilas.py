"""Las pilas guardan elementos de todo tipo, en python pueden combinarse datos, en otros lenguajes no pasa así
    
    Metodos:
        * Push(e): agrega elementos al tope de la pila (last in, first out)
        
        * Pop(): retornar y eliminar el ultimo elemento de la pila (no se puede ejecutar con pilas vacías, se levanta una excepción)
        
        * Top(): retorna el ultimo elemento de la pila (no se puede ejecutar con pilas vacías, se levanta una excepción)
        
    Excepciones:
        * Pila vacía
"""
class PilaVacia(Exception):
    def __init__(self) -> None:
        mensaje: str = "La pila está vacía"
        super().__init__(mensaje)
class LimiteDePila(Exception):
    def __init__(self) -> None:
        mensaje: str = "La pila no puede almacenar más valores"
        super().__init__(mensaje)
class Stack:
    
    def __init__(self, tamaño) -> None:
        self.tamaño: int = tamaño
        self.stack: list = [None for n in range(tamaño)]
        self.index: int = 0
    def __str__(self) -> str:
        return f"{self.stack}"
    
    def push(self, valor) -> None:
        self.stack.pop()
        self.stack.insert(self.index, valor)
        self.tamaño += 1
        self.index += 1

    def pop(self):
        if self.tamaño != 0:
            self.index -= 1
            temp = self.stack[self.index]
            self.stack[self.index] = None            
            self.tamaño -= 1
            return temp
        raise PilaVacia
    
    def top(self):
        if self.tamaño != 0:
            return self.stack[-1]
        raise PilaVacia
    
    def _limite(self):
        if len(self.stack) >= self.tamaño:
            raise LimiteDePila
        return True
            
class Stack2:
    
    def __init__(self) -> None:
        self.stack2: Stack = Stack()
    def __str__(self) -> str:
        return f"{self.stack2}"
    def push(self, valor):
        self.stack2.push(valor)
    def pop(self):
        return self.stack2.stack.pop()
    def top(self):
        return self.stack2.top()
    
"""
E4. Dada una pila llena de colas llenas de caracteres, determine si con los caracteres de estas colas 
se puede formar el string S. Cree una función que reciba esta pila y devuelva True o False con base en la respuesta.
"""

