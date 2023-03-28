from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    nota1: float
    nota2: float
    nota3: float
    nota4: float
    media: float = None

def lerAlunos() -> Aluno:
    nome = input("nome do aluno: ")
    notas = []
    for i in range(1, 5):
        notas.append(float(input(f'Nota {i}: ')))
    return Aluno(nome, notas[0], notas[1], notas[2], notas[3])

def calcularMedia(aluno: Aluno) -> None:
    media = (aluno.nota1 + aluno.nota2 + aluno.nota3 + aluno.nota4) / 4
    aluno.media = media

def situacaoAluno(aluno: Aluno) -> None:
    calcularMedia(aluno)
    if aluno.media < 7:
        print(f'{aluno.nome} esta reprovado\nMedia: {aluno.media}')

aluno1 = lerAlunos()
aluno2 = lerAlunos()
aluno3 = lerAlunos()

situacaoAluno(aluno1)
situacaoAluno(aluno2)
situacaoAluno(aluno3)