import customtkinter as ctk 
from tkinter import PhotoImage, RIGHT

class Telalogin:
    def __init__(self, janela, callback_login):
        self.janela = janela
        self.callback = callback_login
        self.criar_tela_login()

    def criar_tela_login(self):
        self.image = PhotoImage(file="unifimes.png")
        self.label_image = ctk.CTkLabel(master=self.janela, image=self.image, text="")
        self.label_image.place(x=-50, y=-65)

        self.login_frame = ctk.CTkFrame(self.janela, width=350, height=396)
        self.login_frame.pack(side=RIGHT)

        texto = ctk.CTkLabel(self.login_frame, text="Sistema de Login", font=("Roboto", 20))
        texto.place(x=25, y=5)

        username = ctk.CTkEntry(self.login_frame, placeholder_text="Username", width=300, font=("Roboto", 14))
        username.place(x=25, y=105)

        senha = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*", width=300, font=("Roboto", 14))
        senha.place(x=25, y=175)

        checkbox = ctk.CTkCheckBox(self.login_frame, text="Lembrar login")
        checkbox.place(x=25, y=235)

        login_botao = ctk.CTkButton(self.login_frame, text="Login", width=300, command=self.callback)
        login_botao.place(x=25, y=285)

    def esconder_tela_login(self):
        self.login_frame.pack_forget()
        self.label_image.place_forget()

    def reexibir_tela_login(self):
        self.criar_tela_login()