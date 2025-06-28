
class Page:
    def click(self):
        print("clicking...")

    def find_element(self):
        print("finding element...")

    def verify(self):
        print("verifying...")


class LoginPage(Page):
    def login(self):
        print("login...")

class LogoutPage(Page):
    def logout(self):
        print("logout...")

class SignUpPage(Page):
    def signup(self):
        print("signup...")

login_page = LoginPage()
login_page.click()
login_page.verify()

logout_page = LogoutPage()
signup_page = SignUpPage()

