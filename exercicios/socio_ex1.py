from dataclasses import dataclass

@dataclass
class Socio:
    nome: str
    porcentagem: float

def lerSocio(n: int):
    nome = input(f'Nome do socio {n}: ')
    porcentagem = float(input('Sua porcentagem: '))
    return Socio(nome, porcentagem)

def pocentagemSocio(porcentangem: float, valor: float) -> float:
    porcentangem /= 100
    resultado = (valor * porcentangem)
    return resultado

valor = float(input('Valor total da empresa: '))

socios = []

for i in range(3):
    socios.append(lerSocio(i + 1))

for i in range(3):
    print(f'O socio {socios[i].nome} tem R$ {pocentagemSocio(socios[i].porcentagem, valor):.2f} de açoes')