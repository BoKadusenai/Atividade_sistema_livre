# Classe pai, onde estão contidas as informações que são comuns a todos os tipos de animais terrestres
class AnimaisTerrestres:
    # Método com uma informação que é comum a todos os animais terrestres
    def botarOvo(self):
        print("É um animal ovíparo")

    def pele(self):
        print("Possui pele")

    def patas(self):
        print("Possui patas")

# Classe que contém as similaridades apenas dos animais que correm, a classe "AnimaisTerrestres" entre parênteses significa que ela foi herdada pela classe "Correr",
# sendo assim a classe "Correr" tem seus métodos próprios mais os métodos da classe "AnimaisTerrestres"
class Correr(AnimaisTerrestres):
    def correr(self):
        print("É capaz de correr rapidamente")

# Classe que contém as similaridades apenas dos animais que não correm, a classe "AnimaisTerrestres" entre parênteses significa que ela foi herdada pela classe "NãoCorrer",
# sendo assim a classe "NãoCorrer" tem seus métodos próprios mais os métodos da classe "AnimaisTerrestres"
class NãoCorrer(AnimaisTerrestres):
    def nãocorrer(self):
        print("Não é capaz de correr")

# Classes para cada animal terrestre que você deseja representar, essas classes herdam as classes "Correr" ou "NãoCorrer" de acordo com qual característica eles possuem
# e por conseguinte herdam a classe "AnimaisTerrestres"
class Leão(Correr):
    # Método que contém breves informações sobre o animal
    def informações(self):
        print("O leão é um felino majestoso, conhecido por sua juba e reputação como o rei da selva. Eles habitam as savanas da África e são conhecidos por sua caça em grupo e comportamento social.")

class Elefante(Correr):
    def informações(self):
        print("O elefante é o maior mamífero terrestre, reconhecido por suas enormes presas. Eles vivem em várias partes do mundo, incluindo África e Ásia, e são conhecidos por sua inteligência e comportamento social complexo.")

class Girafa(Correr):
    def informações(self):
        print("A girafa é conhecida por seu pescoço longo e elegante, sendo o animal terrestre mais alto do mundo. Elas habitam as savanas da África e se alimentam de folhas das árvores com suas línguas compridas.")

class Tigre(Correr):
    def informações(self):
        print("O tigre é um grande felino, conhecido por suas listras e poder de caça. Eles são encontrados em várias partes da Ásia e são uma espécie ameaçada de extinção.")

class UrsoPanda(Correr):
    def informações(self):
        print("Os ursos pandas são conhecidos por sua pelagem preta e branca e são nativos da China. Eles são herbívoros e se alimentam principalmente de bambu.")

class Zebra(Correr):
    def informações(self):
        print("As zebras são animais terrestres listrados que habitam as savanas da África. Suas listras são únicas para cada indivíduo e servem como camuflagem contra predadores.")

class Rinoceronte(Correr):
    def informações(self):
        print("Os rinocerontes são conhecidos por seus chifres e pele espessa. Eles são encontrados na África e Ásia e estão ameaçados de extinção devido à caça ilegal.")

class Hipopótamo(Correr):
    def informações(self):
        print("O hipopótamo é um animal aquático massivo que habita rios e lagos da África. Eles são conhecidos por sua agressividade e força.")

class Koala(NãoCorrer):
    def informações(self):
        print("O koala é um marsupial australiano conhecido por se alimentar de folhas de eucalipto e dormir a maior parte do dia.")

class PandaVermelho(NãoCorrer):
    def informações(self):
        print("O panda-vermelho é um pequeno mamífero que habita as florestas do Himalaia. Eles são herbívoros e se alimentam principalmente de bambu e frutas.")

class Canguru(NãoCorrer):
    def informações(self):
        print("O canguru é um marsupial saltador nativo da Austrália. Eles são conhecidos por sua habilidade de saltar longas distâncias.")

class Tatu(NãoCorrer):
    def informações(self):
        print("O tatu é um pequeno mamífero coberto de placas ósseas que o protegem de predadores. Eles são encontrados nas Américas e se alimentam de insetos.")

class Coala(NãoCorrer):
    def informações(self):
        print("O coala é um marsupial australiano conhecido por se alimentar de folhas de eucalipto e dormir a maior parte do dia.")

class Orangotango(NãoCorrer):
    def informações(self):
        print("O orangotango é um grande primata encontrado na Indonésia e na Malásia. Eles são conhecidos por sua inteligência e habitat na floresta tropical.")
