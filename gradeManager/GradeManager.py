from tabulate   import tabulate
from colorama   import Fore, Style
from Disciplina import Disciplina
from curso import curso
from Nota import Nota
from aluno import aluno
from professor import professor
import cmd


class CommandInterpreter(cmd.Cmd):                                                        
                                                          
    logo =  Fore.MAGENTA+r"   _____               _      __  __                                   "+"\n"
    logo +=           r"  / ____|             | |    |  \/  |                                  "+"\n"
    logo +=           r" | |  __ _ __ __ _  __| | ___| \  / | __ _ _ __   __ _  __ _  ___ _ __ "+"\n"
    logo +=           r" | | |_ | '__/ _` |/ _` |/ _ \ |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|"+Style.RESET_ALL+"\n"
    logo += Fore.LIGHTCYAN_EX+r" | |__| | | | (_| | (_| |  __/ |  | | (_| | | | | (_| | (_| |  __/ |   "+"\n"
    logo +=           r"  \_____|_|  \__,_|\__,_|\___|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| v1.0 "+"\n"
    logo +=           r"                                                        __/ |          "+"\n"
    logo +=           r"                                                       |___/           "+ "\n"
    logo +=           r"======================================================================="+"\n"
    logo +=           r"                  Bem-vindo ao Gerenciador de Notas.                   "+"\n"
    logo +=           r" Desenvolvido para disciplina de Orientação a objetos do curso de S.I  "+"\n"    
    logo +=           r"======================================================================="+Style.RESET_ALL+"\n"
    intro = logo
    prompt = Fore.LIGHTCYAN_EX+"> "+Style.RESET_ALL
    
    def parseline(self, line):
        # Manipula comandos compostos específicos
        command, arg, line = super().parseline(line)
        
        # Verifica se o comando é "add disciplina" e o mapeia para "add_disciplina"
        if command == "add disciplina":
            command = "add_disciplina"
        
        return command, arg, line

    def do_sair(self, arg):
        "Sair do prorgama"
        print("Saindo...") 
        return True  # Retorna True para encerrar o loop
    def do_add_disciplina(self,arg):           
        Disciplina.add_disciplina(arg)
    def do_add_curso(self,arg):           
        curso.add_curso(arg)
    def do_list(self,arg):
        if arg == 'disciplina':
            Disciplina.list_disciplina()
        elif arg== 'aluno':
            aluno.list_aluno()
        elif arg== 'curso':
            curso.list_curso()
        elif arg== 'professor':
            professor.list_professor()

    def do_delete_disciplina(self,arg):        
        Disciplina.delete_disciplina(arg)
    def do_delete_curso(self,arg):        
        curso.delete_curso(arg)
    def do_update_disciplina(self,arg):            
        Disciplina.update_disciplina(arg)
    def do_update_curso(self,arg):            
        curso.update_curso(arg)
    def do_add_aluno(self,arg):
        def validar_cpf_aluno(cpf):
            cpf = ''.join(filter(str.isdigit, cpf))
            
            if len(cpf) != 11:
                return False, "CPF deve conter 11 dígitos."
            
            soma_digitos = sum(int(digito) for digito in cpf)
            
            faixas_validas = [
                range(10, 13),  
                range(21, 24),  
                range(32, 35),  
                range(43, 46),  
                range(54, 57),  
                range(65, 68),  
                range(76, 79),  
                range(87, 89) 
            ]
            
            for faixa in faixas_validas:
                if soma_digitos in faixa:
                    return True, f"CPF válido."
                return False, f"CPF é inválido."

        nome=input("insira o nome do aluno") 
        cpf=input("insira o nome do cpf") 
        
        valido, mensagem = validar_cpf_aluno(cpf)
        if not valido:
            print(Fore.RED + mensagem + Style.RESET_ALL)
            return 
        
        senha = input("Insira a senha: ")
        telefone=input("insira o nome do telefone") 

        aluno.add_aluno(nome,cpf,senha,telefone)
    def do_add_professor(self, arg):
        def validar_cpf_professor(cpf):
            # Remove caracteres não numéricos
            cpf = ''.join(filter(str.isdigit, cpf))
        
            if len(cpf) != 11:
                return False, "CPF deve conter 11 dígitos."

            soma_digitos = sum(int(digito) for digito in cpf)

            faixas_validas = [
                range(10, 13),  
                range(21, 24),  
                range(32, 35),  
                range(43, 46),  
                range(54, 57),  
                range(65, 68),  
                range(76, 79),  
                range(87, 89)   
            ]

            for faixa in faixas_validas:
                if soma_digitos in faixa:
                    return True, f"CPF é válido."
            return False, f"CPF é inválido."

        nome = input("Insira o nome do professor: ")
        cpf = input("Insira o CPF do professor: ")
    
    # Validação da soma do CPF
        valido, mensagem = validar_cpf_professor(cpf)
        if not valido:
            print(Fore.RED + mensagem + Style.RESET_ALL)
            return

        email = input("Insira o email: ")
        senha = input("Insira a senha: ")
        ID_curso = input("Insira o ID do curso: ")
        
        if not curso.validacao_curso(ID_curso):
            print(Fore.RED + "ID do curso inválido. O curso não existe." + Style.RESET_ALL)
            return
    
        professor.add_professor(nome, cpf, email, senha, ID_curso)
    def do_delete_aluno(self,arg):        
        aluno.delete_aluno(arg)
        
    def do_add_nota(self,arg):
        try:
            ID_professor = int(input("Insira o ID do professor:"))
            if Nota.verificar_id_professor(ID_professor):
                print(Fore.GREEN + f'ID encontrado' + Style.RESET_ALL)
            else:
                print(Fore.RED + f'ID não encontrado' + Style.RESET_ALL)
                return

            ID_aluno = int(input("Insira o ID do aluno:"))
            if Nota.verificar_id_aluno(ID_aluno):
                print(Fore.GREEN + f'ID encontrado' + Style.RESET_ALL)
            else:
                print(Fore.RED + f'ID não encontrado' + Style.RESET_ALL)
                return

            ID_disciplina = int(input("Insira o ID da disciplina:"))
            if Nota.verificar_id_disciplina(ID_disciplina):
                print(Fore.GREEN + f'Disciplina encontrada' + Style.RESET_ALL)
            else:
                print(Fore.RED + f'Disciplina não encontrada' + Style.RESET_ALL)
                return

        except ValueError:
            print(Fore.RED + f'Por favor insira um valor válido' + Style.RESET_ALL)

if __name__ == '__main__':
    CommandInterpreter().cmdloop()