class Aluno:
    def __init__(self, nome: str, nota: float) -> None:
        self.nome = nome
        self.nota = nota

def lerAluno():
    nome = input('Nome do aluno: ')
    idade = int(input('idade: '))
    return Aluno(nome, idade)

