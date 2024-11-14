import sqlite3
from colorama import Fore, Style
from tabulate import tabulate

class curso:

    def add_curso(nome):        
        try:
            # Conecta no banco de dados
            with sqlite3.connect('grademanager.db') as conn:

                cursor=conn.cursor()
        
                cursor.execute('INSERT INTO curso (nome) VALUES (?)', (nome,))        
                result = cursor.fetchone()

                if result:
                    print(Fore.RED + "Falha ao adicionar a nova curso." + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "Nova curso adicionada com sucesso!" + Style.RESET_ALL)   
                
        except Exception as e:
            print(Fore.RED+"Não foi possivel adicionar a nova curso."+Style.RESET_ALL)

    def list_curso():       
        try:
            # Connect to SQLite database
            with sqlite3.connect('grademanager.db') as conn:
                # conn = sqlite3.connect('grademanager.db')
                cursor=conn.cursor()
        
                # Verifique se o nome de usuário e a senha fornecidos correspondem a uma conta no banco de dados
                cursor.execute('SELECT * FROM curso')        
                cursos=cursor.fetchall()
                data = []
                for curso in cursos:
                    data.append([curso[0],curso[1]])

                table = tabulate(data, headers=["ID","Nome"],tablefmt="rounded_grid")

                print(table)

        except Exception as e:
            print(f"Ocorreu o erro:{e}")
    
    def delete_curso(id):
        try:
            with sqlite3.connect('grademanager.db') as conn:
        
                cursor=conn.cursor()
                        
                cursor.execute('DELETE FROM curso WHERE id=?', (id,))
                result = cursor.fetchone()
                if result:
                    print(Fore.RED+"Não foi possivel remover a curso")
                else:
                    print(Fore.GREEN+"Removida com sucesso com sucesso!!"+Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED+"Não foi possivel remover a curso")

    def update_curso(id):
        try:
            with sqlite3.connect('grademanager.db') as conn:                
              
                cursor=conn.cursor()
        
                cursor.execute('SELECT nome FROM curso WHERE id= ? ', (id,))
                
                curso=cursor.fetchall()
            
                if curso:
                
                    print(f"Nome da curso: {curso[0][0]}")

                    nome = input(Fore.CYAN+"Novo nome: "+Style.RESET_ALL)
                
                    cursor.execute('UPDATE curso SET nome = ? WHERE id=?', (nome,id))
                    result2 = cursor.fetchone()
                    if result2:
                        print(Fore.RED+f"curso alterada com sucesso"+Style.RESET_ALL)
                    else:
                        print(Fore.GREEN+f"Não foi possivel editar curso"+Style.RESET_ALL)
                else:
                    print(Fore.RED+f"curso não encontrada"+Style.RESET_ALL)        
             
        except Exception as e:
            print(Fore.RED+f"Não foi possivel editar curso {e}"+Style.RESET_ALL)