from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class LoginScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.username_input = TextInput(multiline=False)
        self.password_input = TextInput(password=True, multiline=False)

        self.add_widget(self.username_input)
        self.add_widget(self.password_input)

        self.submit_button = Button(text="Submit")
        self.submit_button.bind(on_press=self.submit_login)
        self.add_widget(self.submit_button)

    def submit_login(self, instance):
        with open("login.txt", "a") as f:
            f.write(f"Username: {self.username_input.text}, Password: {self.password_input.text}\n")

class LoginApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()