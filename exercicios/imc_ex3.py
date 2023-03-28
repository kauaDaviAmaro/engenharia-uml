from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    peso: float
    altura: float

def lerPessoa() -> Pessoa:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    altura = float(input('altura: '))
    return Pessoa(nome, peso, altura)

def calculeIMC(altura: float, peso: float) -> float:
    imc = peso * altura / altura**2
    return imc

def foraNormal(imc: float) -> bool:
    if imc > 25:
        return True

pessoa1 = lerPessoa()
pessoa2 = lerPessoa()
pessoa3 = lerPessoa()

print(calculeIMC(pessoa1.altura, pessoa1.peso))
print(calculeIMC(pessoa2.altura, pessoa2.peso))
print(calculeIMC(pessoa3.altura, pessoa3.peso))