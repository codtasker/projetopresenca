import pyodbc

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\jpegg\OneDrive\Documentos\teste1.accdb;'
    )

def alunonovo(nome,idazure,classe):
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    str_bd = "insert into aluno(nome,id_azure) values ('"+nome+"','"+idazure+"')"
    crsr.execute(str_bd)
    cnxn.commit()

def retornome(id):
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    print("conected")
    crsr.execute("select id_azure,nome from aluno")
    rows = crsr.fetchall()
    for row in rows:
        if row.id_azure == id:
            print(row.nome,"indentificado")