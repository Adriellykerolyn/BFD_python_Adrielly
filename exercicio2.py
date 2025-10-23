# Construa uma classe carro, ela deve conter:
# 3 Atributos
# 5 Métodos

# class Carro:
#      def __init__(self, modelo, cor, ano):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano
        
        
#         def modelo(self):
#             print(input("Digite o modelo do carro: "))
#             return f"O carro é do modelo {self.modelo}"
        
#         def cor(self):
#             print(input("Digite a cor do carro: "))
#             return f"O carro é da cor {self.cor}"
        
#         def ano(self):
#             print(input("Digite o ano do carro: "))
#             return f"O carro é do modelo {self.ano}"


# Construa uma classe carro, ela deve conter:
# 3 Atributos
# 5 Métodos

# Construa uma classe carro, ela deve conter:
# 3 Atributos
# 5 Métodos

class Carro:
    def _init_(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.ligado = False

    def verificar_modelo(self):
        self.modelo = input("Digite o modelo do carro: ")
        return f"O carro é do modelo {self.modelo}"

    def verificar_cor(self):
        self.cor = input("Digite a cor do carro: ")
        return f"O carro é da cor {self.cor}"

    def verificar_ano(self):
        self.ano = input("Digite o ano do carro: ")
        return f"O carro é do ano {self.ano}"

    def perguntar_estado(self):
        estado = input("O carro está ligado?")
        if estado in ["sim", "Sim", "SIM"]:
            self.ligado = True
            return "O carro está ligado."
        elif estado in ["não", "Não", "NÃO"]:
            self.ligado = False
            return "O carro está desligado. Você deve ligar o carro."
        else:
            return "Resposta inválida. Digite apenas 'sim' ou 'não'."

carro = Carro("", "", "",)
print(carro.verificar_modelo())
print(carro.verificar_cor())
print(carro.verificar_ano())
print(carro.perguntar_estado())
print(f"O carro é do modelo {carro.modelo}, da cor {carro.cor}, do ano {carro.ano}")



