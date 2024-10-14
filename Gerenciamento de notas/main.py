import customtkinter as ctk 
from tkinter import *
from tela_login import Telalogin
from tela_secundaria import TelaSecundaria

janela = ctk.CTk(fg_color="white")

class Application():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.tela_login = Telalogin(self.janela, self.tela_secundaria)
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x400")
        janela.title("Gerenciamento de notas")
        janela.resizable(False, False)
        
    def tela_secundaria(self):
        self.tela_login.esconder_tela_login()
        self.tela_secundaria = TelaSecundaria(self.janela, self.voltar_login)
        
    def voltar_login(self):
        self.tela_secundaria.esconder_tela_secundaria()
        self.tela_login.reexibir_tela_login()
        
Application()
