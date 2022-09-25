class Passageiro:
    def __init__(self, nome, sobrenome, RG, CPF, endereco, celular, fixo, status, assento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.RG = RG
        self.CPF = CPF
        self.endereco = endereco
        self.celular = celular
        self.fixo = fixo
        self.status = status
        self.assento = assento

    def __str__(self):
        return self.nome + " " + self.sobrenome + " - " + self.RG + " - " + self.CPF + " - " + self.endereco + " - " + \
               self.celular + " - " + self.fixo + " - " + self.status + " - " + str(self.assento)


    #Utilizado para ordenação da lista
    def __lt__(self, other):
        return str(self.nome + " " + self.sobrenome) > str(other.nome + " " + other.sobrenome)
