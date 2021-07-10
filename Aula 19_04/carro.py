class Carro():
    def __init__(self, consumoCombust):
        self.consumoCombust = consumoCombust
        self.numCombust = 0

    def andar(self, kmPercorrido):
        global combustGasto
        combustGasto = (kmPercorrido / self.consumoCombust)
        return print(f'Quilometragem percorrida: {kmPercorrido}km\nCombustível gasto: {combustGasto}L')

    def obterGasolina(self):
        global combustGasto
        self.numCombust = self.numCombust - combustGasto
        return print(f'Combustível atual: {self.numCombust} litros')

    def adicionarGasolina(self, qtdAbastecer):
        self.numCombust = self.numCombust + qtdAbastecer
        return print(f'Gasolina adicionada: {qtdAbastecer}L')

meuFusca = Carro(15)
meuFusca.adicionarGasolina(2)
meuFusca.andar(15)
meuFusca.obterGasolina()
