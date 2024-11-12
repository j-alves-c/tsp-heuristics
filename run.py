"""
Main da aplicação: recebe os dados de entrada e invoca as heurísticas
"""

__author__ = "Júlia Alves Corazza e Letícia Yurie Kokubu"
__date__ = "27/06/2022"

from metaheuristicas import HillClimbing
from metaheuristicas import SimulatedAnnealing
from metaheuristicas import BuscaTabu
from estruturas import Grafo
import os


def valida_entrada(option):
    while (not option[0].__eq__("hc_tsp")) and (
        not option[0].__eq__("sa_tsp") and (not option[0].__eq__("bt_tsp"))
    ):
        print("****Heurística incorreta!****")
        return False
    while (
        (option[0].__eq__("hc_tsp") and len(option) != 3)
        or (option[0].__eq__("sa_tsp") and len(option) != 6)
        or (option[0].__eq__("bt_tsp") and len(option) != 4)
    ):
        print("****Número de parâmetros inválido!****")
        return False

    arquivo = option[1]
    arquivo_formatado = f"{arquivo}.tsp.txt"
    arquivos = os.listdir("entrada")
    while arquivo_formatado not in arquivos:
        print("****Arquivo inválido!****")
        return False
    while option[0].__eq__("hc_tsp") and len(option) == 3:
        try:
            float(option[2])
            break
        except ValueError:
            print("****Parâmetro não numérico!****")
            return False
    while option[0].__eq__("sa_tsp") and len(option) == 6:
        try:
            float(option[2])
            float(option[3])
            float(option[4])
            float(option[5])
            while float(option[3]) >= 1.0:
                print("****Taxa de resfriamento deve ser menor que 1!****")
                return False
            break
        except ValueError:
            print("****Parâmetro(s) não numérico(s)****")
            return False
    while option[0].__eq__("bt_tsp") and len(option) == 4:
        try:
            int(option[2])
            int(option[3])
            break
        except ValueError:
            print("****Parâmetro(s) não numérico(s)****")
            return False
    return True


def main():
    option = input("Digite as informações necessárias: ").split(" ")
    if option == ["0"]:
        exit(0)
    while not valida_entrada(option):
        option = input("Digite as informações de forma correta: ").split(" ")
    arquivo = option[1]
    arquivo_formatado = f"{arquivo}.tsp.txt"
    if option[0].__eq__("hc_tsp"):
        grafo = Grafo(f"entrada/{arquivo_formatado}")
        grafo.le_vertices()
        hc = HillClimbing(grafo, int(option[2]))
        distancia, solucao = hc.run()
        print(round(distancia))
    elif option[0].__eq__("sa_tsp"):
        grafo = Grafo(f"entrada/{arquivo_formatado}")
        grafo.le_vertices()
        sa = SimulatedAnnealing(
            grafo, float(option[2]), float(option[3]), int(option[4]), float(option[5])
        )
        distancia, solucao = sa.run()
        print(round(distancia))
    elif option[0].__eq__("bt_tsp"):
        grafo = Grafo(f"entrada/{arquivo_formatado}")
        grafo.le_vertices()
        bt = BuscaTabu(
            grafo, int(option[2]), int(option[3])
        )
        distancia, solucao = bt.run()
        print(round(distancia))


# melhorar as validações: ordem de validações


if __name__ == "__main__":
    main()
