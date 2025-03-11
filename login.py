import flet as ft

users = {"admin": "adminpass",
         "sehyun": "sehyun is cool"}

def main(page: ft.Page):

    def signinfunction(e):
        if usernametext.value not in users.keys():
            users[usernametext.value] = passwordtext.value
        else:
            statusText.value = "This user already exists"
        page.update()

    def loginfunction(e):
        if usernametext.value in users.keys and passwordtext in usernametext.value():
            statusText.value = "Succesful login :)"
        else:
            statusText.value = "Unsuccesful login :("

    usernametext = ft.TextField(hint_text="username")
    passwordtext = ft.TextField(hint_text="password", password=True, can_reveal_password=True)
    signin = ft.ElevatedButton(text= "sign in", on_click= signinfunction)
    login = ft.ElevatedButton(text="Log in", on_click=loginfunction)
    statusText = ft.Text()
    page.add(usernametext, passwordtext, signin, login, statusText)
    page.update()

ft.app(target = main)