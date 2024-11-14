import sqlite3
from colorama import Fore, Style
from tabulate import tabulate
class aluno:
     
     def add_aluno(nome,cpf,telefone,senha):        
        try:
            # Conecta no banco de dados
            with sqlite3.connect('grademanager.db') as conn:

                cursor=conn.cursor()
        
                cursor.execute('INSERT INTO aluno (nome,CPF,telefone,senha) VALUES (?,?,?,?)', (nome,cpf,telefone,senha))        
                result = cursor.fetchone()

                if result:
                    print(Fore.RED + "Falha ao adicionar o novo aluno." + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "Nova aluno adicionada com sucesso!" + Style.RESET_ALL)   
                
        except Exception as e:
            print(Fore.RED+"Não foi possivel aluno a nova disciplina."+Style.RESET_ALL)
     def list_aluno():       
        try:
            # Connect to SQLite database
            with sqlite3.connect('grademanager.db') as conn:
                # conn = sqlite3.connect('grademanager.db')
                cursor=conn.cursor()
        
                # Verifique se o nome de usuário e a senha fornecidos correspondem a uma conta no banco de dados
                cursor.execute('SELECT * FROM aluno')        
                alunos=cursor.fetchall()
                data = []
                for aluno in alunos:
                    data.append([aluno[0],aluno[1],aluno[2],aluno[3]])

                table = tabulate(data, headers=["ID","cpf","Nome","telefone"],tablefmt="rounded_grid")

                print(table)

        except Exception as e:
            print(f"Ocorreu o erro:{e}")
     def delete_aluno(id):
        try:
            with sqlite3.connect('grademanager.db') as conn:
        
                cursor=conn.cursor()
                        
                cursor.execute('DELETE FROM aluno WHERE id=?', (id,))
                result = cursor.fetchone()
                if result:
                    print(Fore.RED+"Não foi possivel remover o aluno")
                else:
                    print(Fore.GREEN+"Removido com sucesso !!"+Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED+"Não foi possivel remover o aluno")


