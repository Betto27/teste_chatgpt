from tkinter import *

def login():
    # aqui você pode verificar se as credenciais de login estão corretas
    # e, se estiverem, pode abrir a próxima janela
    username = entry_user.get()
    password = entry_pass.get()
    with open("login_data.txt", "a") as file:
        file.write(f"{username}, {password}\n")
    print("Login successful!")

# criando a janela
root = Tk()
root.title("Tela de Login")

# criando os widgets
label_user = Label(root, text="Usuário:")
entry_user = Entry(root)

label_pass = Label(root, text="Senha:")
entry_pass = Entry(root, show="*")

button_login = Button(root, text="Login", command=login)

# posicionando os widgets na janela
label_user.grid(row=0, column=0)
entry_user.grid(row=0, column=1)

label_pass.grid(row=1, column=0)
entry_pass.grid(row=1, column=1)

button_login.grid(row=2, column=1)

# exibindo a janela
root.mainloop()