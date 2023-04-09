class User:
    def __init__(self, conn):

        self.conn = conn
        loged = False
        ID = 0
        #cursor.execute("INSERT INTO pessoas (nome,idade,email,senha) VALUES ('Mario', 30, 'mario123@gmail.com', '12345' )")

        def login():
            log = input("Email: ")
            senha = input("Senha: ")

            roda = conn.execute("SELECT ID, email, senha from pessoas")
            
            for row in roda:
                if (row[1] == log) and (row[2] == senha):
                    loged = True
                    print("Conectado")
                    
                    ID = row[0]
                    inp = input("clique 1 para editar user ou lique para 2 para deletar este user: ")
                    if inp == 1:
                        editarUser(ID)
                    elif inp == 2:
                        deletarUser()
                else: 
                    loged = False
                    print("conecxão não efetuada, gostaria de mudar a senha")
                    editarUser(ID)


        def cadastro():

            n = input("nome: ")
            i = int(input("Idade: "))
            e = input("Email: ")
            s = input("Senha: ")

            sql = """ INSERT INTO pessoas (nome,idade,email,senha) VALUES (?, ?, ?, ?) """

            conn.execute(sql, (n, i, e, s))
            conn.commit() 


        def editarUser(id):
            sql = ""
            atribut = ["email", "senha"]

            if loged == True:

                inp = input("Aperte 1 para atualizar email, 2 para atualizar senha ou 3 para ambos: ")
                if inp == 1:
                    e = input("Atualizar email: ")
                    sql = """ UPDATE pessoas SET {:s} = {:s} WHERE ID = {:s} """.format(atribut[0], e, id)
                elif inp == 2:
                    s = input("Atualizar senha: ")
                    sql = """ UPDATE pessoas SET {:d} = {:d} WHERE ID = {:s} """.format(atribut[1], s, id) 
                elif inp == 3:
                    e = input("Atualizar email: ")
                    s = input("Atualizar email: ")
                    sql = """ UPDATE pessoas SET {:s}, {:s}  = {:d}, {:s} WHERE ID = {:s} """.format(atribut[0], atribut[1], e, s, id)
            else:
                inp = input("digite nova senha: ")
            
                cursor = conn.execute("SELECT , senha from pessoas")

                for row in cursor:
                    if (row[0] == inp):
                        print("senha já existente")
                    elif (row[0] != inp):
                        conn.execute("UPDATE pessoas SET senha = {:s} WHERE ID = {:s}".format(inp, id))


            conn.execute(sql)
            conn.commit()
            

        def deletarUser(id):
            conn.execute("DELETE from pessoas where ID = {:s};".format(id))
            conn.commit()
            