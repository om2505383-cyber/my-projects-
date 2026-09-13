class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def view_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"
