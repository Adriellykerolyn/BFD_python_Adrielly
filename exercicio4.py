# Desenvolva um programa que peça o ano de nascimento do usuário e o ano atual, e então calcule e exiba a idade do usuário.

nasc = int(input("Insira o ano do seu nascimento:"))
ano = int(input("Insira o ano atual:"))

calc = ano - nasc

print("A sua idade é:", calc)