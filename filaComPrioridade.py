import heapq
import random
import time

fila_prioridades = []
fila_comum = []

def adicionar_grupo():
    nome = input("Digite o nome da reserva: ")
    qtd_pessoas = int(input("Digite a quantidade de pessoas: "))
    tempo_preparo = int(input("Digite o tempo de preparo em minutos: "))

    if len(fila_prioridades) >= tamanho_fila_prioridades:
        print("Erro: a fila de prioridades está lotada!")
        return

    heapq.heappush(fila_prioridades, (qtd_pessoas, tempo_preparo, nome))

def mostrar_proximo_grupo():
    if not fila_prioridades:
        print("A fila de prioridades está vazia!")
        return

    print("Próximo grupo na fila de prioridades:")
    print("Nome:", fila_prioridades[0][2])
    print("Quantidade de pessoas:", fila_prioridades[0][0])
    print("Tempo de preparo:", fila_prioridades[0][1])

def preparar_proxima_refeicao():
    if not fila_prioridades:
        print("A fila de prioridades está vazia!")
        return

    grupo = heapq.heappop(fila_prioridades)
    fila_comum.append(grupo)

    tempo_espera = grupo[1] + sum([x[1] for x in fila_comum])

    print("Preparando refeição para o grupo:", grupo[2])
    print("Tempo estimado de espera:", tempo_espera, "minutos")

def entregar_refeicao():
    if not fila_comum:
        print("A fila comum está vazia!")
        return

    grupo = fila_comum.pop(0)
    print("Entregando refeição para o grupo:", grupo[2])

def gerar_simulacao():
    num_grupos = int(input("Digite o número de grupos a serem gerados na simulação: "))
    max_fila_prioridades = int(input("Digite o tamanho máximo da fila de prioridades: "))
    
    for i in range(num_grupos):
        nome = "Grupo " + str(i+1)
        qtd_pessoas = random.randint(min_pessoas, max_pessoas)
        tempo_preparo = random.randint(min_tempo_preparo, max_tempo_preparo)
        tupla = (qtd_pessoas, tempo_preparo, nome)
        
        if len(fila_prioridades) < max_fila_prioridades:
            heapq.heappush(fila_prioridades, tupla)
        else:
            print("A fila de prioridades está cheia! Não é possível adicionar o grupo", nome)

def main():
    fila_prioridades = []
    fila_preparo = []
    tamanho_fila_prioridades = 0

    while True:
        time.sleep(1.5)
        
        print("\033[0;00m + + + + + + MENU + + + + + + ")
        print("1) Definir tamanho da fila com prioridades")
        print("2) Adicionar novo grupo na fila com prioridades")
        print("3) Mostrar próximo grupo aguardando")
        print("4) Preparar próxima refeição")
        print("5) Entregar refeição")
        print("6) Gerar simulação")
        print("7) Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            tamanho_fila_prioridades = int(input("\nDigite o tamanho da fila de prioridades: "))
            print("\033[0;32m" + "\n============================================\nTamanho da fila de prioridades definido para:", tamanho_fila_prioridades,"\n============================================")

        elif opcao == 2:
            if len(fila_prioridades) < tamanho_fila_prioridades:
                nome = input("\nDigite o nome do grupo: ")
                qtd_pessoas = int(input("Digite a quantidade de pessoas: "))
                tempo_preparo = int(input("Digite o tempo de preparo em minutos: "))
                novo_grupo = (qtd_pessoas, tempo_preparo, nome)
                heapq.heappush(fila_prioridades, novo_grupo)
                print("\033[0;32m" + "\n==============================\nGrupo adicionado com sucesso!\n==============================")

            else:
                print("\033[1;31m" + "\n A fila de prioridades já está lotada!\n")

        elif opcao == 3:
            if len(fila_prioridades) > 0:
                proximo_grupo = heapq.heappop(fila_prioridades)
                print("\033[1;36m" + "\nPróximo grupo aguardando:")
                print("Nome:", proximo_grupo[2])
                print("Quantidade de pessoas:", proximo_grupo[0])
                print("Tempo de preparo:", proximo_grupo[1], "minutos\n")
                heapq.heappush(fila_prioridades, proximo_grupo)
            else:
                print("\033[1;31m" + "\nA fila de prioridades está vazia!\n")

        elif opcao == 4:
            if len(fila_prioridades) > 0:
                grupo_preparo = heapq.heappop(fila_prioridades)
                tempo_espera = grupo_preparo[1] + sum([x[1] for x in fila_preparo])
                fila_preparo.append(grupo_preparo)
                print("\033[0;32m" "\nPreparando próxima refeição para o grupo:", grupo_preparo[2])
                print("\033[0;32m" "Tempo estimado de espera:", tempo_espera, "minutos \n")
            else:
                print("\033[1;31m" + "\nA fila de prioridades está vazia!\n")

        elif opcao == 5:
            if len(fila_preparo) > 0:
                grupo_entrega = fila_preparo.pop(0)
                print("\033[0;32m" + "\n Refeição entregue para o grupo:", grupo_entrega[2] + "\n")
            else:
                print("\033[1;31m" + "\n A fila de preparo está vazia!\n")
        
        elif opcao == 6:
            num_grupos = int(input("Digite o número de grupos a serem gerados: "))
            min_pessoas = int(input("Digite o número mínimo de pessoas por grupo: "))
            max_pessoas = int(input("Digite o número máximo de pessoas por grupo: "))
            min_tempo = int(input("Digite o tempo mínimo de preparo por grupo: "))
            max_tempo = int(input("Digite o tempo máximo de preparo por grupo: "))

            for i in range(num_grupos):
                nome = "Grupo " + str(i+1)
                qtd_pessoas = random.randint(min_pessoas, max_pessoas)
                tempo_preparo = random.randint(min_tempo, max_tempo)
                grupo = (qtd_pessoas, tempo_preparo, nome)

                try:
                    heapq.heappush(fila_prioridades, grupo)
                except IndexError:
                    print("\033[1;31m" + "Não foi possível adicionar o grupo. A fila de prioridades está cheia.")
            
            print("\033[0;32m" + "Simulação gerada com sucesso!")

        elif opcao == 7:
            break
        else:
            print("\033[1;31m" + "Opção inválida!")

main()