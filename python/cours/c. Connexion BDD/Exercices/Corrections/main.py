class User:
    def __init__(self, tmp2, tmp3):
        self.firstname: str = tmp2
        self.lastname:str = tmp3

    @property
    def fullname(self):
        if self.firstname is not None:
            return self.firstname + " " + self.lastname
        else:
            return self.lastname

    @fullname.setter
    def fullname(self):
        return self.firstname + " " + self.lastname
    
my_user = User("robin", "hotton")
print(my_user.fullname)