class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        name, email, password = string_params.split(",")
        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_params):
        return cls(list_params[0], list_params[1], list_params[2])

user1 = User.from_string("******,********,******")
user2 = User.from_list(["******", "******", "******"])

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)