
from flask_httpauth import HTTPBasicAuth
from flask import Flask, request
from models import Programador, Habilidades, ProgHab, Usuarios
from flask_restful import Resource, Api

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

class Programadores(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Programador.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id,
                'email': pessoa.email
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Pessoa nao encontrada'
            }
        return response
    def put(self,nome):
        pessoa = Programador.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if'idade' in dados:
            pessoa.idade = dados['idade']
        if 'email' in dados:
            pessoa.email = dados['email']
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade,
            'email':pessoa.email
        }
        return response
    def delete(self,nome):
        pessoa = Programador.query.filter_by(nome=nome).first()
        mensagem = 'Programador {} excluido com sucesso!'.format(pessoa.nome)
        pessoa.delete()
        return{'status':'sucesso', 'mensagem':mensagem}

class ListaProgramadores (Resource):
    @auth.login_required
    def get(self):
        pessoas = Programador.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade, 'email': i.email} for i in pessoas]
        return response
    def post(self):
        dados = request.json
        pessoa = Programador(nome=dados['nome'], idade=dados['idade'], email=dados['email'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade,
            'email':pessoa.email
        }
        return response

class ListaHabilidade(Resource):
    @auth.login_required
    def get(self):
        habilidades = Habilidades.query.all()
        response = [{'id':i.id, 'nome':i.nome} for i in habilidades]
        return response
    def post(self):
        dados = request.json
        habilidade = Habilidades(nome=dados['nome'])
        habilidade.save()
        response = {
            'id':habilidade.id,
            'nome':habilidade.nome
        }
        return response

class ProgramadorHab(Resource):
    @auth.login_required
    def get(self):
        proghab = ProgHab.query.all()
        response = [{'id': i.id, 'programador': i.programador.nome, 'habilidades': i.habilidades.nome} for i in proghab]
        return response
    def post(self):
        dados = request.json
        prog = Programador.query.filter_by(nome=dados['pessoa']).first()
        hab = Habilidades.query.filter_by(nome=dados['habilidades']).first()
        proghab = ProgHab(habilidades=hab, programador=prog)
        proghab.save()
        response = {
            'programador': proghab.programador.nome,
            'habilidades': proghab.habilidades.nome,
            'id': proghab.id
        }
        return response
    def delete(self):
        tchau = ProgHab.query.all()
        tchau.delete()
        return {'status': 'sucesso', 'mensagem': 'excluido'}

api.add_resource(Programadores, '/pessoa/<string:nome>/')
api.add_resource(ListaProgramadores, '/listaprog/')
api.add_resource(ListaHabilidade, '/habilidades/')
api.add_resource(ProgramadorHab, '/proghab/')

if __name__ == '__main__':
    app.run(debug=True)