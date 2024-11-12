
from estruturas import Grafo
import random
from collections import deque

class BuscaTabu:
    def __init__(self, grafo, numero_maximo_iteracoes, tamanho_lista_tabu):
        self.grafo = grafo
        self.numero_maximo_iteracoes = numero_maximo_iteracoes
        self.tamanho_lista_tabu = tamanho_lista_tabu
        self.lista_tabu = deque(maxlen=tamanho_lista_tabu)

    def melhor_vizinho(self, vizinhanca, distancia_corrente):
        vizinho_melhor = None
        distancia_melhor = float('inf')

        for vizinho in vizinhanca:
            if vizinho not in self.lista_tabu:
                distancia_vizinho = self.grafo.distancia_percorrida(vizinho)
                if distancia_vizinho < distancia_melhor or (vizinho in self.lista_tabu and distancia_vizinho < distancia_corrente):
                    vizinho_melhor = vizinho
                    distancia_melhor = distancia_vizinho

        return distancia_melhor, vizinho_melhor

    def run(self):
        t = 0
        self.grafo.gera_solucao()
        solucao_corrente = self.grafo.solucao_corrente
        distancia_corrente = self.grafo.distancia_solucao_corrente

        melhor_solucao = solucao_corrente
        melhor_distancia = distancia_corrente

        while t < self.numero_maximo_iteracoes:
            vizinhanca = self.grafo.gera_vizinhanca(solucao_corrente)
            distancia_vizinho, vizinho_melhor = self.melhor_vizinho(vizinhanca, distancia_corrente)

            if vizinho_melhor:
                solucao_corrente = vizinho_melhor
                distancia_corrente = distancia_vizinho

                self.lista_tabu.append(solucao_corrente)

                if distancia_corrente < melhor_distancia:
                    melhor_solucao = solucao_corrente
                    melhor_distancia = distancia_corrente

            t += 1

        return melhor_distancia, melhor_solucao

def main():
    grafo = Grafo('entrada/pr76.tsp.txt')
    grafo.le_vertices()
    busca_tabu = BuscaTabu(grafo, numero_maximo_iteracoes=100, tamanho_lista_tabu=10)
    distancia, _ = busca_tabu.run()
    print(round(distancia))

if __name__ == '__main__':
    main()