"""Classe que representa o grafo. Atributos: arquivo de entrada com a instância de TSP, lista de vértices,
bem como a solução e a distância percorrida da solução encontrada pelas heurísticas. """
__author__ = "Júlia Alves Corazza e Letícia Yurie Kokubu"
__date__ = "29/06/2022"

import math
import os
import random
from typing import Union
from estruturas.vertice import Vertice


class Grafo:

    def __init__(self, entrada: Union[str, bytes, os.PathLike]):
        self.vertices: list[Vertice] = []
        self.solucao_corrente: list[Vertice] = []
        self.distancia_solucao_corrente: float = 0
        self.entrada = entrada

    def le_vertices(self):
        """
    Lê os vértices do grafo a partir do arquivo de entrada.
    """
        vertices = []

        with open(self.entrada, 'r') as arquivo:
            for linha in arquivo.readlines():
                linha = linha.split(' ')

                items = []
                for item in linha:
                    if item not in ('', '\n'):
                        items.append(float(item))

                if items:
                    rotulo, x, y = items

                v = Vertice(int(rotulo), x, y)
                vertices.append(v)
        self.vertices = vertices

    def gera_vizinho(self, solucao, i, k):
        vizinho = [None] * len(solucao)
        for j in range(0, i):
            vizinho[j] = solucao[j]
        for j in range(i, k + 1):
            vizinho[j] = solucao[k - j + i]
        for j in range(k + 1, len(solucao)):
            vizinho[j] = solucao[j]
        return vizinho

    def gera_vizinhanca(self, solucao):
        vizinhanca = []
        for k in range(2, len(solucao) - 2):
            vizinho = self.gera_vizinho(solucao, 1, k)
            vizinhanca.append(vizinho)
        for i in range(2, len(solucao) - 2):
            for k in range(i + 1, len(solucao)):
                vizinho = self.gera_vizinho(solucao, 1, k)
                vizinhanca.append(vizinho)
        return vizinhanca

    def peso_aresta(self, u, v):
        return math.sqrt((u.x - v.x) ** 2 + (u.y - v.y) ** 2)

    def distancia_percorrida(self, solucao):
        distancia = 0
        for i in range(0, len(solucao) - 1):
            distancia += self.peso_aresta(solucao[i], solucao[i + 1])
        distancia += self.peso_aresta(solucao[-1], solucao[0])
        if self.solucao_corrente == solucao:
            self.distancia_solucao_corrente = distancia
        return distancia

    def gera_solucao(self):
        solucao = self.vertices.copy()
        random.shuffle(solucao)
        if len(self.solucao_corrente) == 0:
            self.atribui_solucao(solucao)
        return solucao

    def atribui_solucao(self, solucao):
        self.solucao_corrente = solucao
        self.distancia_percorrida(solucao)