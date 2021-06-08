import dbconnect as db
import reconhece_face as rc
def master():
    while True:
        func = input("1-visualisar alunos 2-cadastrar aluno 3-criar classe 4-criar usuarios 5-sair: ")
        if func == '1':
            db.listarAlunos()
        elif func == '2':
            nome = input("digite o nome: ")
            fl = input("digite a classe: ")
            rc.nr(nome,fl)
        elif func == '3':
            fl = input("digite o nome classe: ")
            rc.nfl(fl)
        elif func == '4':
            while True:
                usuario = input("qual o usuario: ")
                senha = input("qual a senha: ")
                tipo = input("digite o tipo do usuario 1-master 2-codernador 3-professor: ")
                if tipo == "1" or tipo == "2" or tipo == "3":
                    db.criarUsuario(usuario,senha,tipo)
                    break
        elif func == '5':
            break

while True:
    usuario = input("digite seu usuario: ")
    senha = input("digite sua senha: ")
    if db.login(usuario,senha) == 1:
        master()
    break
