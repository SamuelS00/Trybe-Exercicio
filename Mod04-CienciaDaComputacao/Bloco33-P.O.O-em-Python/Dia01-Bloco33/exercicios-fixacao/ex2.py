class Eletrodomestico:
    def __init__(self, cor, potencia, voltagem, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__voltagem = voltagem
        self.__ligado = False
        self.__amperagem_atual_no_motor = 0

    def ligar(self, velocidade):
        self.__velocidade = velocidade
        self.__amperagem_atual_no_motor = (
            (self.__potencia / self.__voltagem) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado

    # Getter
    @property
    def cor(self):
        return self.__cor

    # Setter
    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor


class Liquidificador(Eletrodomestico):  # Exemplo de Herança
    def __init__(self, cor, potencia, voltagem, preco):
        # chamando o método da classe mãe
        super().__init__(cor, potencia, voltagem, preco)


class Geladeira(Eletrodomestico):
    def __init__(self, cor, potencia, voltagem, preco, quantidade_de_portas=1):
        super().__init__(cor, potencia, voltagem, preco)
        # sobrescrita do método da classe mãe
        self.quantidade_de_portas = quantidade_de_portas


class Fogao(Eletrodomestico):
    def __init__(self, cor, potencia, voltagem, preco, quantidade_de_bocas=1):
        super().__init__(cor, potencia, voltagem, preco)
        self.quantidade_de_bocas = quantidade_de_bocas


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.eletrodomesticos = []

    # Permitindo a aquisição de qualquer eletrodoméstico
    def comprar_eletrodomestico(self, eletrodomestico: Eletrodomestico):
        if eletrodomestico.preco >= self.saldo_na_conta:
            self.saldo_na_conta -= eletrodomestico.preco
            self.eletrodomestico.append(eletrodomestico)

    def __str__(self):
        if len(self.eletrodomesticos) > 0:
            return (
                f"possui os seguintes eletrodomésticos {self.eletrodomesticos}"
            )

        return "Não possui"


fogao = Fogao("Preto", "5000", "127", 3000)
geladeira = Geladeira("Branca", "4000", "127", 1400)

pessoa_cozinheira = Pessoa("Jacquin", 5000)
pessoa_cozinheira.comprar_eletrodomestico(fogao)


print(pessoa_cozinheira)
