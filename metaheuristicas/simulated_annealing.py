"""
Classe que representa a heurística Simulated Annealing.
Atributos: grafo, a temperatura máxima, a taxa de decréscimo de temperatura, o número máximo de iterações e a temperatura mínima.
"""
__author__ = "Júlia Alves Corazza e Letícia Yurie Kokubu"
__date__ = "27/06/2022"

from estruturas import Grafo
import math
import random

class SimulatedAnnealing:
  def __init__(self,grafo,temp_max,tx_decrescimo,numero_max_iteracoes,temp_min):
    self.grafo = grafo
    self.temp_max = temp_max
    self.tx_decrescimo = tx_decrescimo
    self.numero_max_iteracoes = numero_max_iteracoes
    self.temp_min = temp_min
  
  def run(self):
   
    self.grafo.gera_solucao()
    while (self.temp_max >= self.temp_min): 
      t = 0
      while (t != self.numero_max_iteracoes): 
        vizinhanca = self.grafo.gera_vizinhanca(self.grafo.solucao_corrente)
        vizinho = vizinhanca[random.randint(0,len(vizinhanca)-1)] 
        distancia_vizinho = self.grafo.distancia_percorrida(vizinho)
        if (distancia_vizinho < self.grafo.distancia_solucao_corrente):
          self.grafo.atribui_solucao(vizinho)
        else: 
          probabilidade_aceitacao = math.exp((self.grafo.distancia_solucao_corrente - distancia_vizinho)/self.temp_max )
          if (random.random() < probabilidade_aceitacao): 
            self.grafo.atribui_solucao(vizinho)
        t +=1 
      self.temp_max  =  self.temp_max * self.tx_decrescimo
      
    return self.grafo.distancia_solucao_corrente,self.grafo.solucao_corrente


def main():
  grafo = Grafo('entrada/pr76.tsp.txt')
  grafo.le_vertices()
  sa = SimulatedAnnealing(grafo,100,0.9,25,10)
  distancia, _ = sa.run()
  print(round(distancia))

if __name__ == '__main__':
  main()
  