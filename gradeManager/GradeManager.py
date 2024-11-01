from tabulate   import tabulate
from colorama   import Fore, Style
from Disciplina import Disciplina
from aluno import aluno
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
    def do_list(self,arg):
        if arg == 'disciplina':
            Disciplina.list_disciplina()
        elif arg== 'aluno':
            aluno.list_aluno()
    def do_delete_disciplina(self,arg):        
        Disciplina.delete_disciplina(arg)
    def do_update_disciplina(self,arg):            
        Disciplina.update_disciplina(arg)
    def do_add_aluno(self,arg):
        nome=input("insira o nome do aluno") 
        cpf=input("insira o nome do cpf") 
        telefone=input("insira o nome do telefone") 
        aluno.add_aluno(nome,cpf,telefone)
    def do_delete_aluno(self,arg):        
        aluno.delete_aluno(arg)
        
    
    
if __name__ == '__main__':
    CommandInterpreter().cmdloop()