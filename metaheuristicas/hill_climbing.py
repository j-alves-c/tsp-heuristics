"""
Classe que representa a heurística Hill Climbing versão Iterativa.
Atributos: grafo e número máximo de iterações 
"""
__author__ = "Júlia Alves Corazza e Letícia Yurie Kokubu"
__date__ = "29/06/2022"

from estruturas import Grafo
import random


class HillClimbing:
    def __init__(self, grafo, numero_maximo_iteracoes):
        self.grafo = grafo
        self.numero_maximo_iteracoes = numero_maximo_iteracoes

    def melhor_vizinho(self, vizinhanca):
        vizinho_melhor = vizinhanca[random.randint(0, len(vizinhanca) - 1)]
        distancia_melhor = self.grafo.distancia_percorrida(vizinho_melhor)
        for vizinho in vizinhanca:
            distancia_vizinho = self.grafo.distancia_percorrida(vizinho)
            if distancia_vizinho < distancia_melhor:
                vizinho_melhor = vizinho
                distancia_melhor = distancia_vizinho
        return distancia_melhor, vizinho_melhor

    def run(self):
        t = 0
        self.grafo.gera_solucao()
        while t != self.numero_maximo_iteracoes:
            local = False
            vertice_candidato = self.grafo.gera_solucao()
            distancia_candidata = self.grafo.distancia_percorrida(
                vertice_candidato)
            while not local:
                vizinhanca = self.grafo.gera_vizinhanca(vertice_candidato)
                distancia_vizinho, vizinho_melhor = self.melhor_vizinho(
                    vizinhanca)
                if distancia_vizinho < distancia_candidata:
                    vertice_candidato = vizinho_melhor
                    distancia_candidata = distancia_vizinho
                else:
                    local = True
            if distancia_candidata < self.grafo.distancia_solucao_corrente:
                self.grafo.atribui_solucao(vertice_candidato)
            t += 1
        return self.grafo.distancia_solucao_corrente, self.grafo.solucao_corrente


def main():
    grafo = Grafo('entrada/pr76.tsp.txt')
    grafo.le_vertices()
    hc = HillClimbing(grafo, 20)
    distancia, _ = hc.run()
    print(round(distancia))


if __name__ == '__main__':
    main()
