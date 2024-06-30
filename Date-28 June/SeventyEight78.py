class abc:
    #You can remove the variable OR variable value u can enter None
    email=None
    Password=None

    def __init__(self, email, Password):
        self.email = email
        self.Password = Password


    def login_confirm(self,):
        if self.Password=="bhagu@123":
            print("The password is correct")
        else:
            print("The password is incorrect")
# This is end of the class

amit=abc("bhagu@gmail.com", "Bhagu@123")
amit.login_confirm()







