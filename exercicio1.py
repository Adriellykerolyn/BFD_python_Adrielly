with open("Geolocalização.txt","w") as arquivo:
    arquivo.write("Niteroi\n")
    arquivo.write("Rio de janeiro\n")
    arquivo.write("Nova Friburgo\n")
    arquivo.write("Cachoeiras de Macacu\n")
    arquivo.write("Itaborai\n")
    
with open("Geolocalização.txt","r") as arquivo:
    print (arquivo.read())

with open("Geolocalização.txt","r") as arquivo:
    print (arquivo.readlines())

with open("Geolocalização.txt","r") as arquivo:
    var = arquivo.readline()
    print(var)

try:
    var = int(input("Digite um número: "))
    print("Funciona!")
except ValueError:
    print("Digite um número inteiro: ")
print ("Continua")

# Construa uma classe aluno, ela deve conter:
# 5 Atributos
# 2 Métodos

class Aluno:
     def __init__(self, nome, email, curso, turma, turno):
        self.nome = nome
        self.email = email
        self.curso = curso
        self.turma = turma
        self.turno = turno 

     def verificar_curso(self):
        return f"O aluno {self.nome} está no curso {self.curso}."
       
     def verificar_turma(self):
       return f"O aluno {self.nome} está no curso {self.turma}."
       
     def verificar_turno(self):
      return f"O aluno {self.nome} está no curso {self.turno}."
        
Aluno1 = Aluno(nome="Maria", email="maria@email.com", curso="Biologia", turma="203", turno="Noturno")
Aluno2 = Aluno(nome="João", email="joao@email.com", curso="Geografia", turma="205", turno="Integral")

print(f"Curso do Aluno 1: {Aluno1.curso}")
print(Aluno1.verificar_curso())
print(Aluno1.verificar_turma())
print(Aluno1.verificar_turno())

print(f"Curso do Aluno 2: {Aluno2.curso}")
print(Aluno2.verificar_curso())
print(Aluno2.verificar_turma())
print(Aluno2.verificar_turno())