from person import Person


class Staff(Person):
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position

    def view_info(self) -> str:
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"Position: {self.position}"
        )
