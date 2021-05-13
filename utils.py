from models import Programador, Habilidades, ProgHab, Usuarios

#Insere Dados na Tabela Programador
def insere_programador():
    pessoa = Programador(nome='Cleber', idade=22, email='cleberfeijo@hotmail.com')
    print(pessoa)
    pessoa.save()

#Realiza consulta na Tabela Programador
def consulta_programador():
    pessoa = Programador.query.all()
    print(pessoa)
    pessoas = Programador.query.filter_by(nome='Renato').first()
    print(pessoas.idade)
    pessoase = Programador.query.filter_by(nome='Renato').first()
    print(pessoase.email)

#Altera dados na Tabela Programador
def altera_programador():
    pessoa = Programador.query.filter_by(nome='Renato').first()
    pessoa.idade = 29
    pessoa.save()

#Exclui dados na Tabela Programador
def exclui_programador():
    pessoa = Programador.query.filter_by(nome='Cleber').first()
    pessoa.delete()

#Insere Dados na Tabela Habilidades
def insere_habilidade():
    hab = Habilidades(nome='C/C++')
    print(hab)
    hab.save()

#Realiza consulta na Tabela Habilidades
def consulta_habilidade():
    lep = Habilidades.query.all()
    print(lep)
    hab = Habilidades.query.filter_by(nome='Python').first()
    print(hab.nome)

#Altera dados na Tabela Habilidades
def altera_habilidade():
    hab = Habilidades.query.filter_by(nome='C/C++').first()
    hab.nome = 'Ruby'
    hab.save()

#Exclui dados na Tabela Habilidades
def exclui_habilidade():
    hab = Habilidades.query.filter_by(nome='Ruby').first()
    hab.delete()

#Consulta o Programador, sua Idade e sua Habilidade
def consulta():
    hab = Habilidades.query.filter_by(nome='C/C++').first()
    pessoa = Programador.query.filter_by(nome='Renato').first()
    print(pessoa.nome, pessoa.idade, hab.nome)

def exclui_tudo():
    hab = ProgHab.query.filter_by(id=4).first()
    hab.delete()

def printar():
    hab = ProgHab.query.all()
    print(hab)

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('rafael', '1234')
    insere_usuario('cleber', '4321')
    consulta_usuarios()
    insere_programador()
    exclui_programador()
    altera_programador()
    consulta_programador()
    insere_habilidade()
    altera_habilidade()
    exclui_habilidade()
    consulta_habilidade()
    consulta()
    #exclui_tudo()
    printar()