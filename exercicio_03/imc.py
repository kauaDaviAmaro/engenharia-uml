from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    peso: float
    altura: float
    imc: float = None

def lerPessoa(n: int) -> Pessoa:
    nome = input(f'Nome da pessoa {n}: ')
    peso = float(input(f'Peso da pessoa {n}: '))
    altura = float(input(f'Altura da pessoa {n}: '))
    return Pessoa(nome, peso, altura)

def calcularIMC(pessoa: Pessoa) -> None:
    pessoa.imc = pessoa.peso / pessoa.altura ** 2

def situacaoIMC(pessoa: Pessoa) -> None:
    calcularIMC(pessoa)
    if pessoa.imc > 25 or pessoa.imc < 18.5:
        print(f'{pessoa.nome} esta com o IMC fora do normal\nIMC: {pessoa.imc}')
    


pessoa1 = lerPessoa(1)
pessoa2 = lerPessoa(2)
pessoa3 = lerPessoa(3)

situacaoIMC(pessoa1)
situacaoIMC(pessoa2)
situacaoIMC(pessoa3)