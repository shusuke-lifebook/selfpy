class Person:
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.firstname == other.firstname and self.lastname == other.lastname
        return False
