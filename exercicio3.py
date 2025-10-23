# Produza uma classe Pessoa com 3 atributos
# Produza 2 classes, Aluno e Professor, elas devem ser filhas de Pessoa.
# Cada uma deve ter no mínimo 2 atributos adicionais e 3 métodos cada.


class Pessoa:
     def __init__(self, nome, email, idade):
        self.nome = nome
        self.email =  email
        self.idade = idade

class Aluno(Pessoa):

    def __init__(self, nome, email, idade, curso, turno):
        super().__init__(nome, email, idade)
        self.curso=curso
        self.turno=turno

    def verificar_detalhes(self):
        return f"O nome do Aluno é {self.nome}, o email do aluno é {self.email}, e ele tem {self.idade} anos"
    
    def verificar_curso(self):
        return f"O Aluno {self.nome}, faz o curso{self.curso}"
    
    def verificar_turno(self):
        return f"O Aluno {self.nome}, é do turno {self.turno}"
    

    
class Professor(Pessoa):

    def __init__(self, nome, email, idade, instituicao, turma):
        super().__init__(nome, email, idade)
        self.instituicao = instituicao
        self.turma = turma

    def verificar_detalhes(self):
        return f"O nome do Professor é {self.nome}, o email dele é {self.email}, e ele tem {self.idade} anos"

    def verificar_nome(self):
        return f"O nome do Professor é {self.nome}"

    def verificar_instituicao(self):
        return f"O Professor {self.nome} dá aula na instituição {self.instituicao}"
    
    def verificar_turma(self):
        return f"O Professor {self.nome}, dá aula para a turma {self.turma}"

Adrielly = Aluno(nome= "Adrielly", email ="adriellykerolyn@gmail.com", idade="24", curso="Python", turno="Noturno")
Pedro = Professor(nome="Pedro", email="pedro@gmail.com", idade="50", instituicao="UFF", turma="300")

print(Adrielly.verificar_detalhes())
print(Adrielly.verificar_curso())
print(Adrielly.verificar_turno())

print(Pedro.verificar_detalhes())
print(Pedro.verificar_nome())
print(Pedro.verificar_instituicao())
print(Pedro.verificar_turma())