import sqlite3

def insere_usuario(cursor, nome, idade, sexo, ano_de_contratação, periodo, salario, cpf):
    try:
        cursor.execute(f"INSERT INTO informacao(nome, idade, sexo, ano_de_contratação, periodo, salario, cpf) VALUES ('{nome}', '{idade}', '{sexo}', '{ano_de_contratação}', '{periodo}', '{salario}', '{cpf}')")
        banco.commit()
        print('Seu cadastro foi concluido!')
    except:
       print('Opa, houve algum erro, tente novamente!')

def seleciona_cadastrado(cursor, nome, cpf):
   cursor.execute(f"SELECT * FROM informacao WHERE nome = '{nome}' AND cpf = '{cpf}'")
   resultado = cursor.fetchall()
   banco.commit()
   return resultado

def todas_pessoas_cadastradas(cursor):
    cursor.execute("SELECT * FROM informacao")
    valores = cursor.fetchall()
    for i in valores:
        print(i)
        print()

def deletar_cadastro(cursor, nome, cpf):
    resposta = cursor.execute(f"DELETE FROM informacao WHERE nome = '{nome}' AND cpf ='{cpf}'")
    banco.commit()
    return resposta

def atualizar_cadastro(cursor, nome, cpf, salario, periodo, ano_de_contratação):
    if salario != None:
        cursor.execute(f"""
        UPDATE informacao
        SET salario = '{salario}'
        WHERE cpf = '{cpf}'
        AND nome = '{nome}'
        """)
        banco.commit()
    elif periodo != None:
        cursor.execute(f"""
        UPDATE informacao
        SET periodo = '{periodo}'
        WHERE cpf = '{cpf}'
        AND nome = '{nome}'
        """)
        banco.commit()
    elif ano_de_contratação != None:
        cursor.execute(f"""
        UPDATE informacao
        SET ano_de_contratação = '{ano_de_contratação}'
        WHERE cpf = '{cpf}'
        AND nome = '{nome}'
        """)
        banco.commit()

if __name__ == "__main__":
    banco = sqlite3.connect('arquivo_tabela.db')
    cursor = banco.cursor() 
    print('BEM VINDO!')
    resposta = ''
    while resposta != 6:
        print('[ 1 ] FAZER O CADASTRO') 
        print('[ 2 ] VERIFICAR SE EXISTE CADASTRO') 
        print('[ 3 ] ALTERAR O CADASTRO') 
        print('[ 4 ] DELETAR O CADASTRO') 
        print('[ 5 ] EXIBIR AS PESSOAS JÁ CADASTRADAS') 
        print('[ 6 ] ENCERRAR O SISTEMA DE CADASTROS')
        resposta = int(input('Digite o número que você deseja: '))
        if resposta == 1:
            nome = input('Digite seu nome: ')
            idade = int(input('Digite sua idade: '))
            sexo = input('Digite seu sexo: [M/F]')
            ano_de_contratação = int(input('Digite o ano que começou a trabalhar na empresa: '))
            periodo = input('Digite o período em que você trabalha: [DIURNO OU NOTURNO]')
            salario = int(input('Qual seu salário?: '))
            cpf = int(input('Digite seu cpf: '))
             

            insere_usuario(banco, nome,  idade, sexo, ano_de_contratação, periodo, salario, cpf)

        if resposta == 2:
            nome = input('Digite seu nome: ')
            cpf = int(input('Digite seu cpf: '))
            resultado = seleciona_cadastrado(cursor, nome, cpf)
            resultado = resultado[0]
            print()
            print(f'''                      O nome é {resultado[0]}
                      A idade é: {resultado[1]}')
                      O sexo é: {resultado[2]}
                      O ano de contratação é: {resultado[3]}
                      O período é: {resultado[4]}
                      O salario é: {resultado[5]}
                      O CPF é: {resultado[6]}''')
            print()
            
        elif resposta == 3:
            nome = input('Digite seu nome: ')
            cpf = int(input('Digite seu cpf: '))

            resultado = seleciona_cadastrado(cursor, nome, cpf)
            if len(resultado) > 0:
                menu_alterar = int(input('''
                SELECIONE QUAL ITEM DESEJA ALTERAR
                [ 1 ] SALARIO
                [ 2 ] PERIODO
                [ 3 ] ANO DE CONTRATAÇÃO
                '''))
                if menu_alterar == 1:
                    salario = int(input('Digite seu novo salário: '))
                    atualizar_cadastro(cursor, nome, cpf, salario, None, None)
                elif menu_alterar == 2:
                    período = int(input('Digite seu novo período: '))
                    atualizar_cadastro(cursor, nome, cpf, None, periodo, None)
                elif menu_alterar == 3:
                    ano_de_contratação = int(input('Digite seu novo ano de contratação: '))
                    atualizar_cadastro(cursor, nome, cpf, None, None, ano_de_contratação)

            else:
                print('Esse cadastro não exite no banco de dados')
        
        elif resposta == 4:
            nome = input('Digite seu nome: ')
            cpf = int(input('Digite seu cpf: '))
            resposta = deletar_cadastro(cursor, nome, cpf)
        
        
        elif resposta == 5:
            todas_pessoas_cadastradas(cursor)

        elif resposta == 6:
            break
        
        elif resposta > 6:
            print('Digite um número válido! ')







