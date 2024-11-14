import sqlite3
from colorama import Fore, Style
from tabulate import tabulate

class Nota:

    def add_nota(ID_professor,ID_aluno,ID_disciplina,Valor,Descricao,Data):        
        try:
            # Conecta no banco de dados
            with sqlite3.connect('grademanager.db') as conn:

                cursor=conn.cursor()

                cursor.execute('INSERT INTO nota (ID_professor,ID_aluno,ID_disciplina,Valor,Descricao,Data) VALUES (?,?,?,?,?,?)', (ID_professor,ID_aluno,ID_disciplina,Valor,Descricao,Data))        

                print(Fore.GREEN + "Nova nota adicionada com sucesso!" + Style.RESET_ALL)

        except Exception as e:
            print(Fore.RED+"Não foi possivel adicionar a nova nota."+Style.RESET_ALL)

    def verificar_id_professor(ID_professor):
        try:
            with sqlite3.connect('grademanager.db') as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT id FROM professor WHERE id = ?', (ID_professor,))
                result = cursor.fetchone()
                
                if result:
                    return True
                else :
                    return False
                
        except Exception as e:
            print(Fore.RED + f'Erro ao verificar o ID do professor' + Style.RESET_ALL)
            return False

    def verificar_id_aluno(ID_aluno):
            try:
                with sqlite3.connect('grademanager.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute('SELECT id FROM aluno WHERE id = ?', (ID_aluno,))
                    result = cursor.fetchone()
                
                    if result:
                        return True
                    else:
                        return False
                
            except Exception as e:
                print(Fore.RED + f'Erro ao verificar ID do aluno' + Style.RESET_ALL)
                return False
        
    def verificar_id_disciplina(ID_diciplina):
            try:
                with sqlite3.connect('grademanager.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute('SELECT id FROM disciplina WHERE id = ?', (ID_diciplina,))
                    result = cursor.fetchone()
                
                    if result:
                        return True
                    else:
                        return False
                
            except Exception as e:
                print(Fore.RED + f'Erro ao verificar ID da disciplina' + Style.RESET_ALL)
                return False