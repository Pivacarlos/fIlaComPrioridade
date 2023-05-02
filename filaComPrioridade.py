import heapq
import random

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

def main():
    fila_prioridades = []
    fila_preparo = []
    tam_fila = 0

    while True:
        print("---- MENU ----")
        print("1) Definir tamanho da fila com prioridades")
        print("2) Adicionar novo grupo na fila com prioridades")
        print("3) Mostrar próximo grupo aguardando")
        print("4) Preparar próxima refeição")
        print("5) Entregar refeição")
        print("6) Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            tam_fila = int(input("Digite o tamanho da fila de prioridades: "))

        elif opcao == 2:
            if len(fila_prioridades) < tam_fila:
                nome = input("Digite o nome do grupo: ")
                qtd_pessoas = int(input("Digite a quantidade de pessoas: "))
                tempo_preparo = int(input("Digite o tempo de preparo em minutos: "))
                novo_grupo = (qtd_pessoas, tempo_preparo, nome)
                heapq.heappush(fila_prioridades, novo_grupo)
            else:
                print("A fila de prioridades já está lotada!")

        elif opcao == 3:
            if len(fila_prioridades) > 0:
                proximo_grupo = heapq.heappop(fila_prioridades)
                print("Próximo grupo aguardando:")
                print("Nome:", proximo_grupo[2])
                print("Quantidade de pessoas:", proximo_grupo[0])
                print("Tempo de preparo:", proximo_grupo[1], "minutos")
                heapq.heappush(fila_prioridades, proximo_grupo)
            else:
                print("A fila de prioridades está vazia!")

        elif opcao == 4:
            if len(fila_prioridades) > 0:
                grupo_preparo = heapq.heappop(fila_prioridades)
                tempo_espera = grupo_preparo[1] + sum([x[1] for x in fila_preparo])
                fila_preparo.append(grupo_preparo)
                print("Preparando próxima refeição para o grupo:", grupo_preparo[2])
                print("Tempo estimado de espera:", tempo_espera, "minutos")
            else:
                print("A fila de prioridades está vazia!")

        elif opcao == 5:
            if len(fila_preparo) > 0:
                grupo_entrega = fila_preparo.pop(0)
                print("Refeição entregue para o grupo:", grupo_entrega[2])
            else:
                print("A fila de preparo está vazia!")

        elif opcao == 6:
            break
        else:
            print("Opção inválida!")

main()