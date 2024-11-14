import sqlite3
from colorama import Fore, Style
from tabulate import tabulate
class professor:
     def add_professor(nome,CPF,email,senha,ID_curso):        
        try:
            # Conecta no banco de dados
            with sqlite3.connect('grademanager.db') as conn:

                cursor=conn.cursor()
        
                cursor.execute('INSERT INTO professor (nome,CPF,email,senha,ID_curso) VALUES (?,?,?,?,?)', (nome,CPF,email,senha,ID_curso))        
                result = cursor.fetchone()

                if result:
                    print(Fore.RED + "Falha ao adicionar o novo professor." + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "Nova professor adicionada com sucesso!" + Style.RESET_ALL)   
                
        except Exception as e:
            print(Fore.RED+"Não foi possivel professor a nova disciplina."+Style.RESET_ALL)
     def list_professor():       
        try:
            # Connect to SQLite database
            with sqlite3.connect('grademanager.db') as conn:
                # conn = sqlite3.connect('grademanager.db')
                cursor=conn.cursor()
        
                # Verifique se o nome de usuário e a senha fornecidos correspondem a uma conta no banco de dados
                cursor.execute('SELECT * FROM professor')        
                professores=cursor.fetchall()
                data = []
                for professor in professores:
                    data.append([professor[0],professor[1],professor[2],professor[3],professor[4],professor[5]])

                table = tabulate(data, headers=["ID","cpf","Nome","email","ID_curso"],tablefmt="rounded_grid")

                print(table)

        except Exception as e:
            print(f"Ocorreu o erro:{e}")
     def delete_professor(id):
        try:
            with sqlite3.connect('grademanager.db') as conn:
        
                cursor=conn.cursor()
                        
                cursor.execute('DELETE FROM professor WHERE id=?', (id,))
                result = cursor.fetchone()
                if result:
                    print(Fore.RED+"Não foi possivel remover o professor")
                else:
                    print(Fore.GREEN+"Removido com sucesso !!"+Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED+"Não foi possivel remover o professor")


