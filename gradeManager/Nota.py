import sqlite3
from colorama import Fore, Style
from tabulate import tabulate

class nota:

    def add_nota(ID_professor,ID_aluno,ID_diciplina,Valor,Descricao,Data):        
        try:
            # Conecta no banco de dados
            with sqlite3.connect('grademanager.db') as conn:

                notar=conn.notar()
        
                notar.execute('INSERT INTO nota (ID_professor,ID_aluno,ID_diciplina,Valor,Descricao,Data) VALUES (?,?,?,?,?,?)', (ID_professor,ID_aluno,ID_diciplina,Valor,Descricao,Data))        
                result = notar.fetchone()

                if result:
                    print(Fore.RED + "Falha ao adicionar a nova nota." + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "Nova nota adicionada com sucesso!" + Style.RESET_ALL)   
                
        except Exception as e:
            print(Fore.RED+"Não foi possivel adicionar a nova nota."+Style.RESET_ALL)

    def list_nota():       
        try:
            # Connect to SQLite database
            with sqlite3.connect('grademanager.db') as conn:
                # conn = sqlite3.connect('grademanager.db')
                notar=conn.notar()
        
                # Verifique se o nome de usuário e a senha fornecidos correspondem a uma conta no banco de dados
                notar.execute('SELECT * FROM nota')        
                notas=notar.fetchall()
                data = []
                for nota in notas:
                    data.append([nota[0],nota[1]])

                table = tabulate(data, headers=["ID","Nome"],tablefmt="rounded_grid")

                print(table)

        except Exception as e:
            print(f"Ocorreu o erro:{e}")
    
    def delete_nota(id):
        try:
            with sqlite3.connect('grademanager.db') as conn:
        
                notar=conn.notar()
                        
                notar.execute('DELETE FROM nota WHERE id=?', (id,))
                result = notar.fetchone()
                if result:
                    print(Fore.RED+"Não foi possivel remover a nota")
                else:
                    print(Fore.GREEN+"Removida com sucesso com sucesso!!"+Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED+"Não foi possivel remover a nota")

    def update_nota(id):
        try:
            with sqlite3.connect('grademanager.db') as conn:                
              
                notar=conn.notar()
        
                notar.execute('SELECT nome FROM nota WHERE id= ? ', (id,))
                
                nota=notar.fetchall()
            
                if nota:
                
                    print(f"Nome da nota: {nota[0][0]}")

                    nome = input(Fore.CYAN+"Novo nome: "+Style.RESET_ALL)
                
                    notar.execute('UPDATE nota SET nome = ? WHERE id=?', (nome,id))
                    result2 = notar.fetchone()
                    if result2:
                        print(Fore.RED+f"Não foi possivel editar nota"+Style.RESET_ALL)
                    else:
                        print(Fore.GREEN+f"nota alterada com sucesso"+Style.RESET_ALL)
                else:
                    print(Fore.RED+f"nota não encontrada"+Style.RESET_ALL)        
             
        except Exception as e:
            print(Fore.RED+f"Não foi possivel editar nota {e}"+Style.RESET_ALL)