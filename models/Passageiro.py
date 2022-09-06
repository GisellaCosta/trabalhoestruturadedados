import string

class Passageiro:
    def __init__(self, nome, sobrenome, Rg, Cpf, endereco, celular, fixo, status, assento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.SetRg(Rg)
        self.SetCpf(Cpf)
        self.endereco = endereco
        self.celular = celular
        self.fixo = fixo
        self.status = status
        self.assento = assento

    def SetRg(self, Rg: string) -> None:
        if (len(Rg) > 8 and len(Rg) < 6):
            return print('Erro ao inserir RG. Tamanho inválido!')
        self.Rg = Rg

    def SetCpf(self, Cpf: string) -> None:
        if (len(Cpf) != 14):
            return print('Erro ao inserir CPF. Tamanho inválido!')
        self.Cpf = Cpf
    
