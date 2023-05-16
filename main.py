from queue import Queue, LifoQueue
from time import sleep
from os import system

def menu():
    system("cls")
    print("MENU PRINCIPAL\n1 - Operações\n2 - Expressão\n0 - Finalizar Programa")
    escolha = input()
    if escolha == '1':
        ops(filaPrincipal)
    elif escolha == '2':
        exp()
    elif escolha == '0':
        system("cls")
        print("Programa encerrado.\n")
        return
    else:
        system("cls")
        print("Opção inválida, retornando ao MENU PRINCIPAL...")
        sleep(1.5)
        menu()

def ops(fp: Queue):
    system("cls")
    print("Operações\n1 - Adicionar Operação à Fila\n2 - Executar Próxima Operação da Fila")
    print("3 - Executar Todas as operações da Fila\n0 - Voltar para o menu principal")
    escolha = input()
    if escolha == '1':
        system("cls")
        print("1 - Adição (+)\n2 - Subtração (-)\n3 - Multiplicação (*)\n4 - Divisão (/)")
        escolha = input()
        if escolha not in ('1', '2', '3', '4'):
            system("cls")
            print("Operação inválida.")
            sleep(1.5)
            ops(filaPrincipal)
        else:
            system("cls")
            print('Digite "fim" para finalizar:')
            fila = Queue()
            fila.put(int(escolha))
            while True:
                valor = input()
                if valor == "fim":
                    break
                else:
                    try:
                        fila.put(int(valor))
                    except ValueError:
                        print("O valor inserido não é um número.")
            if fila.qsize() > 2:
                fp.put(fila)
            ops(filaPrincipal)
    elif escolha == '2':
        system("cls")
        if not fp.empty():
            rodar_fila(fp.get())
            input("Aperte ENTER ")
            ops(filaPrincipal)
        else:
            print("Fila vazia.")
            sleep(1.5)
            ops(filaPrincipal)
    elif escolha == '3':
        system("cls")
        if not fp.empty():
            while fp.qsize() > 0:
                rodar_fila(fp.get())
                sleep(0.5 if fp.qsize() > 0 else 0)
            input("Aperte ENTER ")
            system("cls")
            ops(filaPrincipal)
        else:
            system("cls")
            print("Fila vazia.")
            sleep(1.5)
            ops(filaPrincipal)
    elif escolha == '0':
        menu()
    else:
        system("cls")
        print("Opção inválida.")
        sleep(1.5)
        ops(filaPrincipal)

def rodar_fila(primeiraFila: Queue):
    operacao = primeiraFila.get()
    if operacao == 1:
        soma(primeiraFila)
    elif operacao == 2:
        sub(primeiraFila)
    elif operacao == 3:
        multi(primeiraFila)
    else:
        div(primeiraFila)

def soma(filaCalculo: Queue):
    print("Adição\nValores:", end=' ')
    soma = 0
    while not filaCalculo.empty():
        i = filaCalculo.get()
        print(i, end=", " if 0 < filaCalculo.qsize() else '')
        soma += i
    print("\nResultado:", soma, "\n")
    
def sub(filaCalculo: Queue):
    print("Subtração\nValores:", end=' ')
    sub = i = filaCalculo.get()
    print(i, end=", ")
    while not filaCalculo.empty():
        i = filaCalculo.get()
        print(i, end=", " if 0 < filaCalculo.qsize() else '')
        sub -= i
    print("\nResultado:", sub, "\n")

def multi(filaCalculo: Queue):
    print("Multi\nValores:", end=' ')
    multi = 1
    while not filaCalculo.empty():
        i = filaCalculo.get()
        print(i, end=", " if 0 < filaCalculo.qsize() else '')
        multi *= i
    print("\nResultado:", multi, "\n")

def div(filaCalculo: Queue):
    print("Divisão\nValores:", end=' ')
    div = i = filaCalculo.get()
    print(i, end=", ")
    while not filaCalculo.empty():
        i = filaCalculo.get()
        print(i, end=", " if 0 < filaCalculo.qsize() else '')
        try:
            div /= i
        except ZeroDivisionError:
            pass
    print("\nResultado:", div, "\n")

def exp():
    system("cls")
    exp = input("EXPRESSÃO\nDigite uma expressão (com espaços entre as entidades): ").split(' ')
    pilhaPrincipal = LifoQueue()
    for i in exp:
        if i in ('(', ')', '[', ']', '{', '}'):
            pilhaPrincipal.put(i)
    if not pilhaPrincipal.empty() and verificador_pilha(pilhaPrincipal):
        print("\nVÁLIDA.")
        sleep(3.5)
        menu()
    else:
        print("\nINVÁLIDA.")
        sleep(3.5)
        menu()

def verificador_pilha(pilha: LifoQueue):
    if pilha.qsize() % 2 == 0:
        aux = {
        '(': ')',
        '[': ']',
        '{': '}'
        }
        referencia = None
        comRef = True
        abertos = pilha.qsize() / 2
        sobrando = []
        while pilha.qsize() > 0:
            elemento = pilha.get()
            for i in aux:
                if elemento == aux[i]:
                    referencia = i
                    comRef = True
                    sobrando.append(elemento)
                    break
                elif elemento == i and (elemento != referencia and comRef):
                    return False
                elif elemento == i and aux[i] in sobrando:
                    sobrando.remove(aux[i])
                    abertos -= 1
                    comRef = False
                    break
        if abertos == 0:
            return True
    return False

filaPrincipal = Queue()
menu()
