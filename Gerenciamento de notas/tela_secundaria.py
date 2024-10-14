import customtkinter as ctk 

class TelaSecundaria:
    def __init__(self, janela, callback_voltar):
        self.janela = janela
        self.callback_voltar = callback_voltar
        self.criar_tela_secundaria()
        
    def criar_tela_secundaria(self):
        self.botao_frame2 = ctk.CTkButton(self.janela,text="VOLTAR", command=self.callback_voltar)
        self.botao_frame2.pack(pady=10)

    def esconder_tela_secundaria(self):
        self.botao_frame2.pack_forget()
