# tsp-heuristics

O código foi feito na linguagem Python,versão 3.8, mas é compilável desde a versão 3.7 até a 3.10.10

Para executar a aplicação, abra o terminal na pasta raiz do projeto e execute: python run.py

A entrada de dados deve seguir o seguinte padrão:
{heuristica} {nome_parcial_do_arquivo} {parametro1} {parametro2} ....

As heurísticas aceitas na aplicação são HillClimbing, Simulated Annealing e Busca Tabu(hc_tsp,sa_tsp e bt_tsp, respectivamente).

Os arquivos de teste estão localizados no diretório entrada e são: att48.tsp.txt, berlin52.tsp.txt,bier127.tsp.txt, eil76.tsp.txt,kroA100.tsp.txt, kroE100.tsp.txt, pr76.tsp.txt, rat99.tsp.txt, st70.tsp.txt

O nome parcial se refere ao prefixo antes de .tsp.txt, o que de fato diferencia o nome dos arquivos de entrada.

Os parâmetros e o número de parâmetros é intrinsecamente relacionado à heurística escolhida. A entrada de parâmetros de forma não númerica não será aceita, assim como a entrada de uma quantidade incorreta de parâmetros.

Assim, um exemplo de entrada para a aplicação seria:

-> Para HillCLimbing: hc_tsp pr76 50

-> Para Simulated Annealing: sa_tsp rat99 1000 0.2 50 1

-> Para Busca Tabu: bt_tsp rat99 1000 2

Algumas instâncias têm sua execução muito morosa, como a bier127 e a kroA100 (Para 20 iterações de Hill Climbing, bier127 levou entre 10 e 14 minutos). A aplicação demora, mas executa.
O tempo de execução variou dentre as ferramentas usadas para a confecção do código. Certas instâncias demoraram mais de 30 minutos no repl.it, mas isso devido ao congestionamento do servidor do repl.it. Nos terminais de PyCharm e VSCode, o tempo foi consideravelmente menor, ainda que continue lenta.

Após a realização de casos de testes, ficou evidente que o Simulated Annealing roda as instâncias de forma mais ágil se comparado com o Hill Climbing. Isso ocorre porque a segunda metaheurística gasta muito tempo gerando e percorrendo todas as vizinhanças.
