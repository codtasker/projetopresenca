import pyodbc

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\jpegg\OneDrive\Documentos\teste1.accdb;'
    )

def alunonovo(nome,idazure,classe):
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    str_bd = "insert into aluno(nome,id_azure,classe) values ('"+nome+"','"+idazure+"',"+classe+")"
    crsr.execute(str_bd)
    cnxn.commit()

def retornome(id):
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    crsr.execute("select id_azure,nome from aluno")
    rows = crsr.fetchall()
    for row in rows:
        if row.id_azure == id:
            print(row.nome,"indentificado")

def login(usuario,senha):
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    crsr.execute("select usuario,senha,tipo_usuario from usuarios")
    rows = crsr.fetchall()
    for row in rows:
        if row.usuario == usuario:
            if row.senha == senha:
                if row.tipo_usuario == 1:
                    print("conectado master ",row.tipo_usuario)
                elif row.tipo_usuario == 2:
                    print("conectado cordenador ",row.tipo_usuario)
                elif row.tipo_usuario == 3:
                    print("conectado professor ",row.tipo_usuario)
                return row.tipo_usuario
    else: return 0

def listarAlunos():
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    crsr.execute("select id_aluno,nome,id_azure,classe from aluno")
    rows = crsr.fetchall()
    print("con es")
    for row in rows:
        print(row.id_aluno," nome: ",row.nome," classe: ",row.classe,"id da azure: ",row.id_azure)

def criarUsuario(usuario,senha,tipo):
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    str_bd = "insert into usuarios(usuario,senha,tipo_usuario) values ('"+usuario+"','"+senha+"',"+tipo+")"
    crsr.execute(str_bd)
    cnxn.commit()