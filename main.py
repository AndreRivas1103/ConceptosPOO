import math
class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


class Circulo:
    def __init__(self, radio: int, centro: Punto):
        self.radio: int = radio
        self.centro: Punto = centro

    def calcular_area(self) -> float:
        return math.pi * self.radio ** 2

    def contiene_punto(self, punto: Punto) -> bool:
        (punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2 <= self.radio ** 2
