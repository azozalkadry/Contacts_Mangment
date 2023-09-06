import uuid


class Contacts:
    def __init__(self, unique_id, name, number, email):
        self.id = unique_id
        self.name = name
        self.number = number
        self.email = email
