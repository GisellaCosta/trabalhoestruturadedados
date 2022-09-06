# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



#from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import ListNode
#from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import SinglyLinkedListIterator
from listaDuplamenteEncadeada import DoubleinkedListIterator
from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import *

# ================ Lista de Exercícios sobre TAD Lista Simplesmente Encadeada ============
from passageiro import Passageiro

""""
1) def print_lista(lista):   OK
2) def maior_elemento(lista): OK
3) def maior_menor_elemento(lista): OK
4) Verificar se duas listas são iguais. Duas listas são iguais se ambas as estruturas têm o mesmo 
número de elementos, e estes são iguais um a um. Em particular, duas listas vazias são iguais. 
def iguais_listas(lst1, lst2): OK 
5) def adicionar_final_lista(lst1, data): OK
6) def insLista(lst1, data): # insere um elemento no inicio da lista OK
7) def concatLista(lst1, lst2): # concatenar a lst2 no final da lst1
8) def esta_na_lista(lst:SinglyLinkedListIterator, data):
9) def estaOrdenada(lst:SinglyLinkedListIterator): # ordem crescente
10) Verificar se uma lista lst2 está contida numa lista lst1. 
    def contidaLista(lst1, lst2):
11) def invLista(lst:SinglyLinkedListIterator): # inverter uma lista lst, destruindo a lista original
"""

def print_lista(lista):
    #verificar se a lista esta vazia ou cheia
    if lista.size == 0:
        print('A lista esta vazia \n')
    else:
        # lista esta cheia
        # por o iterador sobre o primeiro noh da lista
        lista.iterator = lista.firstNode
        #percorrer a lista
        while lista.iterator:
            # printar o atributo data
            print(f' {lista.iterator.data}')
            #avancar o iterador para o proximo noh
            lista.iterator = lista.iterator.nextNode


def maior_elemento(lista):
    # verificar se a lista tem elementos
    # caso a lista tenha elementos fazer:
    # declarar uma variavel: maior
    # atribuir para maior um elemento da sua lista: o primeiro elemento
    # por o iterador sobre o primeiro noh da lista
    # percorrer a lista verificando se o valor armazenado no noh corrente é maior do que o valor
    # armazeando na variavel "maior". Caso seja maior, atualizar a variavel "maior" com
    # o valor corrente do noh.
    # depois avancar o iterador para o proximo no.
    # ao sair do loop retornar o valor armazenado em maior.
    if(lista.size > 0):
        maior = lista.firstNode.data
        lista.iterator = lista.firstNode
        while lista.iterator:
            if lista.iterator.data > maior:
                maior = lista.iterator.data
            lista.nextNode() # ou lista.iterator = lista.iterator.nextNode
        return maior


    # < 1 -> 2 -> 4 -> 5 >
def maior_menor_elemento(lista: SinglyLinkedListIterator):
        if (lista.size > 0):
            maior = lista.firstNode.data
            menor = lista.firstNode.data
            lista.first_Node() # OU lista.iterator = lista.firstNode
            while lista.iterator:
                if lista.iterator.data > maior:
                    maior = lista.iterator.data
                if lista.iterator.data < menor:
                    menor = lista.iterator.data
                lista.nextNode()  # ou lista.iterator = lista.iterator.nextNode
            return [maior, menor]
        else:
            return [None, None]


def iguais_listas(lst1: SinglyLinkedListIterator, lst2: SinglyLinkedListIterator):
    if(lst1.size == 0 and lst2.size == 0):
        return True
    elif (lst1.size != lst2.size):
        return False
    else:
        # as duas listas tem a mesma quantidade de elementos
        # por o iterador da lista 1 sobre o primeiro noh da lista 1
        lst1.first_Node() # ou lst1.iterator = lst1.firstNode
        # por o iterador da lista 2 sobre o primeiro noh da lista 2
        lst2.first_Node()  # ou lst2.iterator = lst2.firstNode
        # percorrer as duas listas simultaneamente:
        while lst1.iterator:
            if lst1.iterator.data != lst2.iterator.data:
                return False
            else:
                #avancar o iterador para proximo noh
                lst1.nextNode() # OU lst1.iterator = lst1.iterador.nextNode
                lst2.nextNode() # OU lst2.iterator = lst2.iterador.nextNode
        return True # as duas listas sao iguais


def adicionar_final_lista(lst1: SinglyLinkedListIterator, data):
    lst1.last_Node() # ou lst1.iterator = lst1.lastNode
    lst1.addNode(data)


def adicionar_final_lista_lento(lst1: SinglyLinkedListIterator, data):
    if(lst1.size == 0):
        lst1.addNode(data)
    else:
        lst1.last_Node() # ou lst1.iterator = lst1.lastNode
        lst1.addNode(data)


def insLista(lst1: SinglyLinkedListIterator, data): # insere um elemento no inicio da lista
    lst1.first_Node() # ou lst1.iterator = lst1.firstNode
    lst1.insNode(data)

def insLista_lentor(lst1: SinglyLinkedListIterator, data): # insere um elemento no inicio da lista
    if(lst1.size == 0):
        lst1.insNode(data)
    else:
        lst1.first_Node() # ou lst1.iterator = lst1.firstNode
        lst1.insNode(data)


def concatLista(lst1: SinglyLinkedListIterator, lst2: SinglyLinkedListIterator): # concatenar a lst2 no final da lst1
    # por iterador da lista 1 no ultimo elemento
    lst1.last_Node()  # ou lst1.iterator = lst1.lastNode
    # por o iterador da lista 2 no primeiro elemento
    lst2.first_Node()  # ou lst2.iterator = lst2.firstNode
    # percorrer a lista 2
    while lst2.iterator:
        # adiciono o elemento do iterador no final da lista 1
        lst1.addNode(lst2.iterator.data)
        # avancar o iterador da lista 2 para o proximo noh
        lst2.nextNode()  # OU lst2.iterator = lst2.iterador.nextNode

# verificar se o elemento data esta presente na lista lst.
# se data estiver presente, retornar True, caso contrario, False
def esta_na_lista(lst:SinglyLinkedListIterator, data):
    # se a lista estiver vazia, data nao esta nela
    if lst.size == 0:
        return False
    else:
        # a lista tem pelo menos um elemento
        # percorrer a lista
        lst.first_Node() # ou lst.iterator = lst.firstNode
        while lst.iterator:
            if lst.iterator.data == data:
                return True # encontrou o elemento
            else:
                # avanca o iterador para o proximo elemento
                lst.nextNode() # ou lst.iterator = lst.iterator.nextNode
        #ao sair do loop pode-se retornar False pois o elemento nao esta na lista
        return  False


def estaOrdenada(lst:SinglyLinkedListIterator): # ordem crescente
    if lst.size == 0 or lst.size == 1: # ou lst.size <= 1
        return True
    else:
        lst.first_Node() # ou lst.iterator = lst.iterator.firstNode
        elemento_anterior = lst.iterator.data
        # avancar o iterador para o proximo elemento
        lst.nextNode() # ou lst.iterator = lst.iterator.nextNode
        # percorrer a lista: tem 2 ou mais nos
        while lst.iterator:
            if elemento_anterior > lst.iterator.data:
                return False
            else:
                # salvar em elemento_anterior o valor do elemento do iterador
                elemento_anterior = lst.iterator.data
                # avanco o iterador para o proximo noh
                lst.nextNode() # ou lst.iterator = lst.iterator.nextNode
        # ao sair do loop a lista so pode estar ordenada em ordem crescente
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    novo_noh = ListNode(5)
    novo_noh.setData(10)
    lista22 = SinglyLinkedListIterator(novo_noh)

    passageiro1 = Passageiro("murilo","ribeiro","1234567","12345678900","vila velha","988653298","33445899","mantido","1")
    passageiro2 = Passageiro("icaro", "juarez", "1244167", "55555678900", "vila velha", "994554598", "31125599", "mantido", "2")
    passageiro3 = Passageiro("maria", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "3")
    passageiro4 = Passageiro("caio", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "4")
    passageiro5 = Passageiro("joão", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "5")
    passageiro6 = Passageiro("marcos", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "6")
    passageiro7 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "7")
    passageiro8 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "8")
    passageiro9 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "9")
    passageiro10 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "10")
    passageiro11 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "11")
    passageiro12 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "12")
    passageiro13 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "13")
    passageiro14 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "14")
    passageiro15 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "15")
    passageiro16 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "16")
    passageiro17 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "17")
    passageiro18 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "18")
    passageiro19 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "19")
    passageiro20 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "20")
    passageiro21 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "21")
    passageiro22 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "22")
    passageiro23 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "23")
    passageiro24 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "24")
    passageiro25 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "25")
    passageiro26 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "26")
    passageiro27 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "27")
    passageiro28 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "28")
    passageiro29 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "29")
    passageiro30 = Passageiro("murilo", "ribeiro", "1234567", "12345678900", "vila velha", "988653298", "33445899", "mantido", "30")

    listaPassageiro = DoubleinkedListIterator()
    listaPassageiro.addNode(10)
    listaPassageiro.addNode(20)
    listaPassageiro.addNode(30)
    listaPassageiro.addNode(40)

    listaEspera = SinglyLinkedListIterator()
    listaEspera.addNode(10)
    listaEspera.addNode(20)
    listaEspera.addNode(30)
    listaEspera.addNode(40)


