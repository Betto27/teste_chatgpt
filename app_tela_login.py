from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
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


class LoginApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()