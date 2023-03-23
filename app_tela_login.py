'''from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

import hashlib


class LoginScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username_input = TextInput(multiline=False, hint_text="Enter username")
        self.password_input = TextInput(password=True, multiline=False, hint_text="Enter password")
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)

        self.feedback_label = Label(text="")
        self.add_widget(self.feedback_label)

        self.submit_button = Button(text="Submit")
        self.submit_button.bind(on_press=self.submit_login)
        self.add_widget(self.submit_button)

    def submit_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        # validate inputs
        if len(username) < 5 or len(password) < 5:
            self.feedback_label.text = "Username and password must be at least 5 characters long"
            return

        if not all(c.isalnum() or c.isspace() for c in username):
            self.feedback_label.text = "Username can only contain letters, numbers, and spaces"
            return

        # hash password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with open("users.txt", "a") as f:
            f.write(f"Username: {username}, Password: {hashed_password}\n")

        self.feedback_label.text = "Login submitted successfully"
        self.parent.add_widget(PersonalInfoScreen())


class PersonalInfoScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = "10dp"
        self.padding = "10dp"

        self.name_input = TextInput(multiline=False, hint_text="Enter name")
        self.phone_input = TextInput(multiline=False, hint_text="Enter phone number")
        self.address_input = TextInput(multiline=False, hint_text="Enter address")
        self.add_widget(self.name_input)
        self.add_widget(self.phone_input)
        self.add_widget(self.address_input)

        self.submit_button = Button(text="Submit")
        self.submit_button.bind(on_press=self.submit_info)
        self.add_widget(self.submit_button)

    def submit_info(self, instance):
        name = self.name_input.text
        phone = self.phone_input.text
        address = self.address_input.text

        with open("users.txt", "a") as f:
            f.write(f"Name: {name}, Phone: {phone}, Address: {address}\n")

        self.parent.remove_widget(self)


class LoginApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.listview import ListView, ListItemButton

class TelaLogin(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Criando caixas de texto para entrada de nome de usuário e senha
        self.caixa_usuario = TextInput(multiline=False)
        self.caixa_senha = TextInput(password=True, multiline=False)

        # Adicionando as caixas de texto à tela de login
        self.add_widget(Label(text="Nome de usuário:"))
        self.add_widget(self.caixa_usuario)
        self.add_widget(Label(text="Senha:"))
        self.add_widget(self.caixa_senha)

        # Criando botão para enviar informações de login
        self.botao_login = Button(text="Enviar")
        self.botao_login.bind(on_press=self.enviar_login)
        self.add_widget(self.botao_login)

        # Criando lista vazia para armazenar informações do usuário
        self.info_usuario = []

    def enviar_login(self, instance):
        # Verificando se as informações de login estão corretas
        if self.caixa_usuario.text == "admin" and self.caixa_senha.text == "admin":
            # Limpando tela de login
            self.clear_widgets()

            # Criando a tela de informações do usuário
            self.tela_info_usuario = BoxLayout(orientation="vertical")

            # Criando campos de entrada para informações do usuário
            self.caixa_nome = TextInput(multiline=False, hint_text="Nome completo")
            self.caixa_telefone = TextInput(multiline=False, hint_text="Telefone")
            self.caixa_endereco = TextInput(multiline=False, hint_text="Endereço")

            # Criando botão para enviar informações do usuário
            self.botao_enviar_info = Button(text="Enviar informações")
            self.botao_enviar_info.bind(on_press=self.enviar_info)

            # Adicionando campos de entrada e botão à tela de informações do usuário
            self.tela_info_usuario.add_widget(Label(text="Preencha suas informações pessoais:"))
            self.tela_info_usuario.add_widget(self.caixa_nome)
            self.tela_info_usuario.add_widget(self.caixa_telefone)
            self.tela_info_usuario.add_widget(self.caixa_endereco)
            self.tela_info_usuario.add_widget(self.botao_enviar_info)

            # Adicionando a tela de informações do usuário à tela principal
            self.add_widget(self.tela_info_usuario)

        else:
            # Caso as informações de login estejam incorretas, mostra mensagem de erro
            self.add_widget(Label(text="Nome de usuário ou senha incorretos"))

    def enviar_info(self, instance):
        # Armazenando as informações do usuário na lista de informações
        self.info_usuario.append(self.caixa_nome.text)
        self.info_usuario.append(self.caixa_telefone.text)
        self.info_usuario.append(self.caixa_endereco.text)

        # Mostrando mensagem de sucesso e limpando campos de entrada
        self.add_widget(Label(text="Informações enviadas com sucesso!"))
        self.caixa_nome.text = ""
        self.caixa_telefone.text = ""
        self.caixa_endereco.text = ""

class AppLogin(App):

    def build(self):
        return TelaLogin()

if __name__ == '__main__':
    AppLogin().run()
