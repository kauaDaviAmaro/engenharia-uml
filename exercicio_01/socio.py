from dataclasses import dataclass

@dataclass
class Socio:
    nome: str
    porcentagem: float

def lerSocio(n: int) -> Socio:
    nome = input(f'Nome do socio {n}: ')
    porcentagem = float(input('Sua porcentagem: '))
    return Socio(nome, porcentagem)

def porcentagemSocio(socio: Socio, valorTotal: float) -> None:
    porcen = (valorTotal * socio.porcentagem) / 100
    print(f'O socio {socio.nome} tem R$ {porcen:.2f} de açoes')

valorTotal = float(input('Valor total da empresa: '))

socio1 = lerSocio(1)
socio2 = lerSocio(2)
socio3 = lerSocio(3)

porcentagemSocio(socio1, valorTotal)
porcentagemSocio(socio2, valorTotal)
porcentagemSocio(socio3, valorTotal)