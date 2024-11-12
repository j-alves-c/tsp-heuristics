"""
Classe que representa o grafo.
Atributos: rótulo, coordenada cartesiana x, coordenada cartesiana y.
"""
__author__ = "Júlia Alves Corazza e Letícia Yurie Kokubu"
__date__ = "27/06/2022"

class Vertice:
    def __init__(self, rotulo: int, x: float, y: float):
        self.rotulo = rotulo
        self.x = x
        self.y = y
