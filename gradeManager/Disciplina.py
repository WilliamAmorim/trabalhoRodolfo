import sqlite3
from colorama import Fore, Style
from tabulate import tabulate

class Disciplina:

    def add_disciplina(nome):        
        try:
            # Conecta no banco de dados
            with sqlite3.connect('grademanager.db') as conn:

                cursor=conn.cursor()
        
                cursor.execute('INSERT INTO disciplina (nome) VALUES (?)', (nome,))        
                result = cursor.fetchone()

                if result:
                    print(Fore.RED + "Falha ao adicionar a nova disciplina." + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "Nova disciplina adicionada com sucesso!" + Style.RESET_ALL)   
                
        except Exception as e:
            print(Fore.RED+"Não foi possivel adicionar a nova disciplina."+Style.RESET_ALL)

    def list_disciplina():       
        try:
            # Connect to SQLite database
            with sqlite3.connect('grademanager.db') as conn:
                # conn = sqlite3.connect('grademanager.db')
                cursor=conn.cursor()
        
                # Verifique se o nome de usuário e a senha fornecidos correspondem a uma conta no banco de dados
                cursor.execute('SELECT * FROM disciplina')        
                disciplinas=cursor.fetchall()
                data = []
                for disciplina in disciplinas:
                    data.append([disciplina[0],disciplina[1]])

                table = tabulate(data, headers=["ID","Nome"],tablefmt="rounded_grid")

                print(table)

        except Exception as e:
            print(f"Ocorreu o erro:{e}")
    
    def delete_disciplina(id):
        try:
            with sqlite3.connect('grademanager.db') as conn:
        
                cursor=conn.cursor()
                        
                cursor.execute('DELETE FROM disciplina WHERE id=?', (id,))
                result = cursor.fetchone()
                if result:
                    print(Fore.RED+"Não foi possivel remover a disciplina")
                else:
                    print(Fore.GREEN+"Removida com sucesso com sucesso!!"+Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED+"Não foi possivel remover a disciplina")

    def update_disciplina(id):
        try:
            with sqlite3.connect('grademanager.db') as conn:                
              
                cursor=conn.cursor()
        
                cursor.execute('SELECT nome FROM disciplina WHERE id= ? ', (id,))
                
                disciplina=cursor.fetchall()
            
                if disciplina:
                
                    print(f"Nome da Disciplina: {disciplina[0][0]}")

                    nome = input(Fore.CYAN+"Novo nome: "+Style.RESET_ALL)
                
                    cursor.execute('UPDATE disciplina SET nome = ? WHERE id=?', (nome,id))
                    result2 = cursor.fetchone()
                    if result2:
                        print(Fore.RED+f"Disciplina alterada com sucesso"+Style.RESET_ALL)
                    else:
                        print(Fore.GREEN+f"Não foi possivel editar disciplina"+Style.RESET_ALL)
                else:
                    print(Fore.RED+f"Disciplina não encontrada"+Style.RESET_ALL)        
             
        except Exception as e:
            print(Fore.RED+f"Não foi possivel editar disciplina {e}"+Style.RESET_ALL)